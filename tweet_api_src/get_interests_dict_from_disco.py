import json
from disco_utils import *
import numpy as np
import pandas as pd
import operator

# Yangzhenchuan Zou (Young Zou)

# returns: a dict as { '<tweet_id>' : [list of interests], ... }
def get_interests_from_discovery(location_query):
    discovery = get_disco()
    env_id = get_environment_id(discovery)
    collection_id = get_collection_id(discovery, env_id)
    
    # For each document, only returns id and enriched_tweets.categories.label
    response_tweets = discovery.query(env_id,
                                      collection_id,
                                      qopts={'filter': {'location_query:\"%s\"' % location_query}},
                                      count=100,
                                      return_fields='id, handle, location, location_query, enriched_tweets.categories.label').get_result()

    return _make_interests_dict(response_tweets, location_query)


def _make_interests_dict(response_tweets, location_query):
    # Load stop words
    with open('tweet_api_src/stopwords.txt', 'r') as stopwords_file:
        stopwords_set = {line.strip() for line in stopwords_file}

    # Crop the query response and frame it with pandas DataFrame
    res_df = pd.DataFrame(response_tweets['results']).drop('result_metadata', axis=1)

    user_interests_dict = {}

    for index, row in res_df.iterrows():
        tweet_id = row['handle']
        label_list = row['enriched_tweets']['categories']
        
        if not 'location_query' in row or row['location_query'] != '\"%s\"' % location_query:
            continue

        location = ''
        if 'location' in row:
            location = row['location']
        
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
        user_interests_dict[tweet_id] =  {
            'interests': result_interests_list,
            'location': location
        }
    
    return user_interests_dict
