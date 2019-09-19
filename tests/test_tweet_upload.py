'''
NOTE: Run this from the top-level directory
'''

import os
from os.path import join

import sys
sys.path.insert(0, join(os.getcwd(), 'tweet_api_src'))

from upload_all_user_tweets_to_discovery import upload_tweets_to_discovery

def test_upload_no_list():
	assert upload_tweets_to_discovery(0) == 0

def test_upload_empty_list():
	assert upload_tweets_to_discovery(1) == 0

def test_upload_no_dict():
	tweets = [0]
	assert upload_tweets_to_discovery(tweets) == 0

def test_upload_empty_dict():
	tweets = [{}]
	assert upload_tweets_to_discovery(tweets) == 0

def test_upload_valid_dict():
	tweets = [{
		'user': {
			'screen_name': '@test_handle',
			'id_str': 'test_id',
			'location': 'test_location'
		},
		'text': 'test tweet'
	}]
	assert upload_tweets_to_discovery(tweets) == 1