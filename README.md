## Steps to run Spark Structured Streaming

- Generate your access keys from [Twitter Dev site](https://developer.twitter.com/apps).
- Add credentials in the **tweetConfig.py** file.
- Start the **Zookeeper** server on terminal followed by **Kafka** server.
- Run **tweetListener.py** file.
- Run **tweetAnalyzer.py** file.

#

## Output

- Running **tweetListener.py** will fetch the tweets in real-time:
<img src=Output/tweetListener.png height=”100” >

- Running **tweetAnalyzer.py** will generate the following output from time to time in batches:
<img src= Output/tweetAnalyzer.png height=”100” >

#

## Error Solving

- While execution, you might get errors which are mainly compatibility issues. To tackle those, use the anything **less than Python 3.8** and also install **PySpark==2.4.6**, and **py4j==1.10.7**.
- If you get an error saying, **Cannot load data source: Kafka** or **refer Structured Streaming + Kafka Integration Guide**, download the jars given [here](https://jar-download.com/artifacts/org.apache.spark/spark-sql-kafka-0-10_2.11/2.4.0/source-code) and extract them in **$SPARK_HOME/jars/**.
