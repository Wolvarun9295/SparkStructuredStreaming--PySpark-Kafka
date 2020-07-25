## Steps to run Spark Structured Streaming

- Generate your access keys from [Twitter Dev site](apps.twitter.com)
- Add credentials in the tweetConfig.py file
- Start the Zookeeper server on terminal followed by Kafka server
- Run tweetListener.py file
- Run tweetAnalyzer.py

## Output will be diplayed as follows

- Running tweetListener.py will fetch the tweets in real-time:
<img src=Output/tweetListener.png height=”100” >

- Running tweetAnalyzer.py will generate the following output from time to time in batches:
<img src= Output/tweetAnalyzer.png height=”100” >
