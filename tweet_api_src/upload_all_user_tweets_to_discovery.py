import json
from ibm_watson import DiscoveryV1

apikey = '0xn8K3fpjG6WKz3SGuXuZQvsmnV1OVhjMAUxnMbx0MUV'
discovery = DiscoveryV1(
    version='2019-04-30',
    iam_apikey=apikey,
    url='https://gateway-wdc.watsonplatform.net/discovery/api'
)
environments = discovery.list_environments().get_result()
environment_id = environments['environments'][1]['environment_id']
print("Loading tweet data")
tweets_raw = []
for line in open('twitter_cache.txt', 'r'):
    tweets_raw.append(json.loads(line))

#print(tweets_raw[3])
#created_at, id_str, text, location, geo, coordinates, place, screen_name, timestamp
document= {"handle":"uninitialized","tweets":""}

#collection_names = {}
collections = discovery.list_collections(environment_id).get_result()
collection_id = ""
print("creating collection if necessary")
if len(collections['collections'])==0:
	new_collection = discovery.create_collection(environment_id=environment_id, name='tweets').get_result()
	collection_id = new_collection['collection_id']
else:

	#
	collection_id = collections['collections'][0]['collection_id']

screen_name = ""
count = 0
for tweet in tweets_raw:
	if ('user_id' not in document):
		screen_name = tweet['user']['screen_name']
		document.update({'user_id':tweet['user']['id_str'], 'handle':screen_name, 'location':tweet['user']['location']})
	document.update({"handle":screen_name})
	if (len(document['tweets'])==0):
		document.update({'tweets':tweet['text']})
	else:
		document.update({'tweets':document['tweets']+ "\n\n"+tweet['text']})
	#document['tweets'].update({'timestamp':tweet['timestamp_ms'], 'created_at':tweet['created_at'], 'tweet_id':tweet['id_str'], 'text':tweet['text'], 'geo':tweet['geo'], 'coordinates':tweet['coordinates'], 'place':tweet['place']})

	print("added tweet" + str(count))
	count+=1
	if (count>=100):
		break;
print(document)
discovery.add_document(environment_id, collection_id, file=json.dumps(document), filename=screen_name, file_content_type='application/json')
print("uploaded document")
