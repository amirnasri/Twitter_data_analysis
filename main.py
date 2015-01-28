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

word_counts = {}

def process_twitt(twitt):
    twitt_json = json.loads(twitt)
    text = twitt_json['text']
    print(text)
    words = text.strip().split()
    for w in words:
        word_counts[w] += 1
        
    for (w, count) in word_counts:
        print("%s: %d" % w, count)
        
class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def __init__(self):
        self.invocation_count = 0
    
    def on_data(self, data):
        print('fdfsa')
        process_twitt(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=[u'basketball'])
    