from tweet_handler import Handler
import json
# tweets = Handler.get_tweets_by_location("40.68402,-73.95704,50km, #ColumbiaUniversity")
# for t in tweets:
#     print(t.text + '\n')

# test get_tweets_by_user
file = open("./handlertest.txt", 'a+')
tweets = Handler.get_tweets_by_user('TeamFiveGuys2')
for t in tweets:
    file.write(json.dumps(t._json) + '\n')
    
# test get_tweets_by_location
tweets = Handler.get_tweets_by_location("40.68402,-73.95704,50km, #Columbia")
for t in tweets:
    print(t.text)