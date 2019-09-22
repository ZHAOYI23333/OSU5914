from ibm_watson import DiscoveryV1

def get_environment_id(discovery):
	result = discovery.list_environments().get_result()
	if not 'environments' in result:
		return None

	environments = result['environments']
	if len(environments) < 2:
		return None

	environment = environments[1]
	if not 'environment_id' in environment:
		return None

	return environment['environment_id']


def get_collection_id(discovery, environment_id):
	result = discovery.list_collections(environment_id).get_result()
	if not 'collections' in result:
		return None

	collections = result['collections']
	collection = None

	if len(collections) == 0:
		print('Creating collection')
		collection = discovery.create_collection(environment_id=environment_id, 
												 name='tweets').get_result()
	else:
		collection = collections[0]

	if collection is None:
		return None

	if not 'collection_id' in collection:
		return None

	return collection['collection_id']

def get_disco():
	return DiscoveryV1(
        version = "2019-08-20",
        iam_apikey='0xn8K3fpjG6WKz3SGuXuZQvsmnV1OVhjMAUxnMbx0MUV',
        url='https://gateway-wdc.watsonplatform.net/discovery/api'
    )

#filename is the handle
def get_document_filename(doc_id):
	disco = get_disco()
	env_id = get_environment_id(disco)
	return disco.get_document_status(env_id, get_collection_id(disco,env_id), doc_id).result['filename']

#filename is the handle, pass in list of all docs
def get_document_id_from_filename(all_users, filename):
	for user, interests in all_users.items():
		handle = get_document_filename(user)
		if handle == filename:
			return user
	return "File not found"
	