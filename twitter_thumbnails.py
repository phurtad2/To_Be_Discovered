from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import requests
import json
import os
from cs_key import *

# Variables that contains the user credentials to access Twitter API


#This is a basic listener that just prints received tweets to stdout.
k = 0
class StdOutListener(StreamListener):
    def on_data(self, data):
        global k
        tweet = json.loads(data)
        bool = True
        try:
            print(tweet['user']['name'])
            url = tweet['user']['profile_image_url'];
            print(tweet['text'])
        except KeyError:
            return bool

        k = k + 1
        with open("twitter_thumbnails/TW_" + str(k), 'wb') as handle:
            response = requests.get(url, stream=True)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)

        return bool





    def on_error(self, status):
        print("error")
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    name1 =  'e' # input("Enter first query: ")
    # name2 = input("Enter second query: ")


    stream.filter(track=['a', 'e', 'i', 'o', 'u'], languages=["en"])
    print("Maximum Size Reached")
