import sys
sys.path.insert(0, 'tweet_api_src')

from tweet_handler import get_tweets_by_location, get_users_by_tweets, upload_all_tweets_of_users
from get_interests_dict_from_disco import get_interests_from_discovery
import json
# tweets = Handler.get_tweets_by_location("40.68402,-73.95704,50km, #ColumbiaUniversity")
# for t in tweets:
#     print(t.text + '\n')

# test get_tweets_by_user

'''
file = open("./handlertest.txt", 'a+')
tweets = Handler.get_tweets_by_user('TeamFiveGuys2')
for t in tweets:
    file.write(json.dumps(t._json) + '\n')
    
# test get_tweets_by_location
tweets = Handler.get_tweets_by_location("40.68402,-73.95704,50km, #Columbia")
for t in tweets:
    print(t.text)
'''

location_query = "Columbus, OH"
#coords = "40.68402,-73.95704,50km"
coords = "39.9611111,-82.9988889,50km"
tweets = get_tweets_by_location(coords)
users = get_users_by_tweets(tweets)
upload_all_tweets_of_users(users, location_query)
interest_json = get_interests_from_discovery(location_query)
print(interest_json)