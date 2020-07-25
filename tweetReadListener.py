from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import twitterConfig
import pykafka

# Grabbing Keys
API_Key = twitterConfig.API_Key
API_SecretKey = twitterConfig.API_SecretKey
Access_Token = twitterConfig.Access_Token
Access_SecretToken = twitterConfig.Access_SecretToken

# Authorizing access
authentication = OAuthHandler(API_Key, API_SecretKey)
authentication.set_access_token(Access_Token, Access_SecretToken)


# Listening to Twitter Stream
class TweetListener(StreamListener):
    def __init__(self):
        self.client = pykafka.KafkaClient("localhost:9092")
        self.producer = self.client.topics[bytes('twitter', 'utf-8')].get_producer()

    def on_data(self, data):
        try:
            jsonData = json.loads(data)
            words = jsonData['text'].split()
            ls = list(filter(lambda x: x.lower().startswith('#'), words))
            if len(ls) != 0:
                for word in ls:
                    print(word)
                    self.producer.produce(bytes(word, 'utf-8'))
            return True
        except KeyError:
            return True

    def on_error(self, status):
        print(status)
        return True


# Filtering tweets
twitterStream = Stream(authentication, TweetListener())
twitterStream.filter(languages=['en'], track=['a', 'e', 'i', 'o', 'u'])
