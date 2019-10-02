import json
from ibm_watson import DiscoveryV1
from disco_utils import *


def upload_tweets_to_discovery(tweet_list):
	'''
	:param tweet_list: A list of tweets where each tweet needs to be formatted as:
		{
			'user': {
				'screen_name': <screen_name>,
				'id_str': <id_str>,
				'location': <location>
			},
			'text': <text>
		}

	:returns An integers representing the number of tweets added to discovery
	'''
	if type(tweet_list) != list:
		return 0

	apikey = '0xn8K3fpjG6WKz3SGuXuZQvsmnV1OVhjMAUxnMbx0MUV'
	discovery = DiscoveryV1(
	    version='2019-04-30',
	    iam_apikey=apikey,
	    url='https://gateway-wdc.watsonplatform.net/discovery/api'
	)
	environment_id = get_environment_id(discovery)
	if environment_id is None:
		return 0

	collection_id = get_collection_id(discovery, environment_id)
	if collection_id is None:
		return 0

	document = { 
		"handle": "uninitialized",
		"tweets": ""
	}

	num_tweets_added = 0
	screen_name = None

	for i, tweet in enumerate(tweet_list):
		#tweet = tweet._json
		if type(tweet) != dict or not all(['user' in tweet, 'text' in tweet]):
			continue

		user = tweet['user']

		if type(user) != dict or not all(['screen_name' in user, 'id_str' in user, 'location' in user]):
			continue

		num_tweets_added += 1

		username = user['screen_name']
		if screen_name is None:
			screen_name = username
		elif screen_name != username:
			return 0

		if not 'user_id' in document:
			document.update({ 
				'user_id': user['id_str'], 
				'handle': username, 
				'location': user['location'] 
			})

		document.update({
			"handle": username
		})


		document['tweets'] = document['tweets'] + '||' + tweet['text']
		#print(document['tweets'])
		# document.update({
		# 	'tweets': document_text
		# })

		#print('Added tweet %d' % i)

		if i >= 100:
			break;

	if screen_name is None:
		return 0

	#print(document)
	print(screen_name)

	#For testing purposes
	if (screen_name=="@test_handle"):
		return num_tweets_added
	discovery.update_document(environment_id, 
						   collection_id, 
						   screen_name,
						   file=json.dumps(document), 
						   filename=screen_name, 
						   file_content_type='application/json')

	print("uploaded document")

	return num_tweets_added
