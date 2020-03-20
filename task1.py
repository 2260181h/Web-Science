#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "1172639268520566785-6IDQ57QSbjIOAYZXUSxoTmrTkQMIMh"
access_token_secret = "oDjP6lPhV0lIdsRE1PfK1M8Oy7glpMWjJzWTUR1jVMDsO"

consumer_key = "N6rP4p2YijBdAnZ7qvpIWS74P"
consumer_secret = "qjgz9aNkarFquBalCsPvr8dT1IPUNkKBUkzM8w8OaoTXSTetLI"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'nhs', 'badminton', 'Glasgow'
    stream.filter(track=['nhs', 'badminton', 'Glasgow'])
