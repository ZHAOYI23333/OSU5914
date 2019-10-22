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

x = discovery.query(environment_id, collection_id, count=200)
#print(x.result)
for doc in x.result['results']:
	#y = discovery.get_document_status(environment_id, collection_id, doc['id']).result['filename']
	#print(y)
	#print(doc['id'])
	#if (y=="@test_handle"):
		#print("you will be yeeted")
	print(discovery.delete_document(environment_id, collection_id, doc['id']).get_result())
