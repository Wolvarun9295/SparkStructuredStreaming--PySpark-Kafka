from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import os
import findspark

# initialize spark
findspark.init("/usr/local/spark/")
os.environ["PYSPARK_PYTHON"] = '/usr/bin/python3'

if __name__ == "__main__":
    spark = SparkSession.builder.appName("KafkaSparkStructuredStreaming").getOrCreate()
    kafkaDF = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe",
                                                                                                           "twitter").load()
    kafkaDF_String = kafkaDF.selectExpr("CAST(value AS STRING)")
    tweetsTable = kafkaDF_String.alias("tweets")
    groupingHashtags = tweetsTable.groupBy("value").count().orderBy(desc("count"))
    query = groupingHashtags.writeStream.outputMode("complete").format("console").start()
    query.awaitTermination()
