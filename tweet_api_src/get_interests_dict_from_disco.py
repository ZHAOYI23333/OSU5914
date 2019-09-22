import json
from tweet_api_src.disco_utils import *
import numpy as np
import pandas as pd
import operator

# Yangzhenchuan Zou (Young Zou)

# returns: a dict as { '<tweet_id>' : [list of interests], ... }
def get_interests_from_discovery():
    discovery = get_disco()
    env_id = get_environment_id(discovery)
    collection_id = get_collection_id(discovery, env_id)
    
    # For each document, only returns id and enriched_tweets.categories.label
    response_tweets = discovery.query(env_id,
                                      collection_id,
                                      count = 100,
                                      return_fields='id, enriched_tweets.categories.label').get_result()
    
    print("Interests Extraction Completed")

    return _make_interests_dict(response_tweets)


def _make_interests_dict(response_tweets):
    # Load stop words
    with open('tweet_api_src/stopwords.txt', 'r') as stopwords_file:
        stopwords_set = {line.strip() for line in stopwords_file}

    # Crop the query response and frame it with pandas DataFrame
    res_df = pd.DataFrame(response_tweets['results']).drop('result_metadata', axis=1)

    user_interests_dict = {}

    for index, row in res_df.iterrows():

        tweet_id = row['id']
        label_list = row['enriched_tweets']['categories']
        
        word_dict = {}

        for label_item in label_list:
            label = label_item['label'].replace('/', ' ').split()
            # Word count
            for word in label:
                if word in word_dict: 
                    word_dict[word] = word_dict[word] + 1
                else:
                    word_dict[word] = 1

        # Sort keywords by frequency
        sorted_interests = sorted(word_dict, key=word_dict.get, reverse=True)

        result_interests_list = []
        
        # Filter out stop words
        for interest in sorted_interests:
            if (not interest in stopwords_set):
                result_interests_list.append(interest)


        # Append result dictionary
        user_interests_dict[tweet_id] = result_interests_list
    
    return user_interests_dict
