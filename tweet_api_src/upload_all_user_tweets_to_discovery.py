import json
from ibm_watson import DiscoveryV1

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
	environments = discovery.list_environments().get_result()
	environment_id = environments['environments'][1]['environment_id']

	print("Loading tweet data")

	collections = discovery.list_collections(environment_id).get_result()
	collection_id = ""
	print("creating collection if necessary")

	collection = None

	if not 'collection' in collections or len(collections['collections']) == 0:
		collection = discovery.create_collection(environment_id=environment_id, name='tweets').get_result()
	else:
		collection = collections['collections'][0]

	if collection is None:
		return 0

	collection_id = collection['collection_id']

	document= { 
		"handle": "uninitialized",
		"tweets": ""
	}

	num_tweets_added = 0

	for i, tweet in enumerate(tweet_list):
		if type(tweet) != dict or not all(['user' in tweet, 'text' in tweet]):
			continue

		user = tweet['user']

		if type(user) != dict or not all(['screen_name' in user, 'id_str' in user, 'location' in user]):
			continue

		num_tweets_added += 1

		screen_name = user['screen_name']

		if not 'user_id' in document:
			document.update({ 
				'user_id': user['id_str'], 
				'handle': screen_name, 
				'location': user['location'] 
			})

		document.update({
			"handle": screen_name
		})

		document_text = tweet['text']

		if 'tweet' in document and len(document['tweets']) > 0:
			document_text = document['tweets'] + '\n\n' + document_text

		document.update({
			'tweets': document_text
		})

		print("added tweet" + str(count))

		if i >= 100:
			break;

	print(document)

	discovery.add_document(environment_id, 
						   collection_id, 
						   file=json.dumps(document), 
						   filename=screen_name, 
						   file_content_type='application/json')

	print("uploaded document")

	return num_tweets_added
