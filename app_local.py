from flask import Flask, jsonify, request
from match_interests import get_most_alike_to_user
from tweet_api_src.get_interests_dict_from_disco import get_interests_from_discovery
from tweet_api_src.disco_utils import *
import json

#app = Flask(__name__, static_url_path='/static')

#@app.route('/')
def index():
	return app.send_static_file('index.html')

#@app.route('/user/<handle>')
def user(handle):
	tweet_list = get_tweets_by_user(handle)

	upload_tweets_to_discovery(tweet_list)
	
	return 200

#@app.route('/friends_and_interests/<handle>/<location>')
def friends_and_interests(handle, location):
	all_users = get_interests_from_discovery()
	most_alike_users = get_most_alike_to_user(handle, all_users)
	doc_id = get_document_id_from_filename(all_users, handle)
	interests = all_users[doc_id]
	interests_json = {}

	for x in interests:
		interests_json[x] = x
	return {
		'friends': most_alike_users[0],
		'interests': interests_json
			}, 200
