# Import the necessary package to process data in JSON format
import time
import json
import tweepy

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1164524078012567553-HaxSlY5hVPk4qe2pUz8uIO6slOuLtk'
ACCESS_SECRET = '7e6t522SsLnuLRrgi1BAPfeHKenI2szYZJlU5dCWvXirf'
CONSUMER_KEY = 'aHs6zOvpLSj3ZwDXRCiRX92d3'
CONSUMER_SECRET = 'aebxhRekPV9FVTNwNz5MOHMJVQf624etNj5K8khhfWUDXfm2OT'

# Setup tweepy to authenticate with Twitter credentials:

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# Create the api to connect to twitter with your creadentials
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
#---------------------------------------------------------------------------------------------------------------------
# wait_on_rate_limit= True;  will make the api to automatically wait for rate limits to replenish
# wait_on_rate_limit_notify= Ture;  will make the api  to print a notification when Tweepyis waiting for rate limits to replenish
#---------------------------------------------------------------------------------------------------------------------

class StreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # store tweet data into file as json
        if not status.retweeted:
            file.write(json.dumps(status._json)+'\n')

    def on_error(self, status_code):
        if status_code == 420:
            return False

# store data into cache_us.txt. Append mode
file = open("../data/cache_us.txt", 'a+')

stream_listener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=stream_listener)

# Get random smaples from stream
stream.sample()
file.close()

