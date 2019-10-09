# Import the necessary package to process data in JSON format
import time
import json
import tweepy
from twitter import *
from upload_all_user_tweets_to_discovery import upload_tweets_to_discovery

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '1164524078012567553-HaxSlY5hVPk4qe2pUz8uIO6slOuLtk'
ACCESS_SECRET = '7e6t522SsLnuLRrgi1BAPfeHKenI2szYZJlU5dCWvXirf'
CONSUMER_KEY = 'aHs6zOvpLSj3ZwDXRCiRX92d3'
CONSUMER_SECRET = 'aebxhRekPV9FVTNwNz5MOHMJVQf624etNj5K8khhfWUDXfm2OT'


# Input: either a twitter id or nickname
# Output: list of tweet object. Can use tweet.text to get content
# Example:  tweets = Handler.get_tweets_by_user('taylorswift13')
def get_tweets_by_user(user_handler):
    tweets = []
    # Create Oath & api class object
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    # handling twitter user & user page information
    user = api.get_user(user_handler)
    user_page = api.user_timeline(user_handler)

    # processing data
    for tweet in user_page:
        # disable RT
        if tweet.user.id == user.id and tweet.text[0:2] != 'RT':
            tweets.append(tweet._json)
    return tweets
    
# Input: string of "latitude, longtitude, radius(unit km or mi) [,#hashtag]" 
# Output: list of tweet objects
# Example: tweets = Handler.get_tweets_by_location("40.68402,-73.95704,50km, #Columbia")
def get_tweets_by_location(location_handler):
    tweets = []
    # Create Oath & api class object
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    # handling twitter user & user page information
    # user_page = api.user_timeline(user_handler)   
    for tweet in api.search(geocode = location_handler, lang="en", count = 50):
        if tweet.text[0:2] != 'RT':
            tweets.append(tweet)

    return tweets

def get_users_by_tweets(tweets):
	return set([tweet._json['user']['screen_name'] for tweet in tweets])

def upload_all_tweets_of_users(users, location_query):
	for user in users:
		user_tweets = get_tweets_by_user(user)
		upload_tweets_to_discovery(user_tweets, location_query)