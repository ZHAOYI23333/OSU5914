from get_interests_dict_from_disco import get_interests_from_discovery
from upload_all_user_tweets_to_discovery import upload_tweets_to_discovery
from tweet_handler import get_tweets_by_user

tweet_list = get_tweets_by_user("KyloR3n")
upload_tweets_to_discovery(tweet_list)
#interests = get_interests_from_discovery()
#print(interests)