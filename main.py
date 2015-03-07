'''
Created on Jan 27, 2015

@author: amir
'''

from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="zAw59fE9CjvdZmPT3sSx1dZfZ"
consumer_secret="PnW6G2GSirN3maBl4DEQKzScEVxs6aFf32lzPADAvXXlnlfAzO"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="2614878294-SQ8VpfJ2In7J3AKsxKtSFNh9zWRUF91McBcEwrb"
access_token_secret="8S1KbktnjOvBQVSlFDWWZlWXCxDrikrtCxxZBXDQ1AYz7"


class Twitt_listener(StreamListener):
    """ A listener that handles twitts that are the received from the twitter streaming API.
        Receives twitt_num number of twitts and appends them to twitt_list
    """
    def __init__(self, twitt_list, twitt_num):
        self.invocation_count = 0
        self.twitt_list = twitt_list
        self.twitt_num = twitt_num
    
    def on_data(self, data):
        self.invocation_count += 1
        if (self.invocation_count == self.twitt_num):
            return False

        self.twitt_list.append(data)
        print("twitt %d" % self.invocation_count)
        return True

    def on_error(self, status):
        print(status)


class Twitt_analyzer():
    def __init__(self, twitt_list):
        self.word_counts = {}

        for twitt in twitt_list:
            self.process_twitt(twitt)
        # Sort word_counts dictionary based on values
        sorted_counts = sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)
        for item in sorted_counts:
            print("%s: %d" % item)

    def process_twitt(self, twitt):
        twitt_json = json.loads(twitt)
        if ('text' not in twitt_json):
            return
        
        # Only consider english twitts
        if ('lang' not in twitt_json) or (twitt_json['lang'] != 'en'):
            return
    
        text = twitt_json['text']
            
        words = text.strip().split()
        for w in words:
            if w in self.word_counts:
                self.word_counts[w] += 1
            else:
                self.word_counts[w] = 1
    
     
if __name__ == '__main__':

        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        twitt_list =[]
        stream = Stream(auth, Twitt_listener(twitt_list, 1000))
        stream.filter(track=['obama'])

        twitt_analyzer = Twitt_analyzer(twitt_list)
    
    
