from flask import Flask, jsonify, request
from match_interests import get_most_alike_to_user

import os
from os.path import join
import sys
sys.path.insert(0, join(os.getcwd(), 'tweet_api_src'))

from get_interests_dict_from_disco import get_interests_from_discovery
from upload_all_user_tweets_to_discovery import upload_tweets_to_discovery
from tweet_handler import get_tweets_by_user
from disco_utils import *
import json

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/user/<handle>', methods=['GET','POST'])
def user(handle):
	tweet_list = get_tweets_by_user(handle)
	upload_tweets_to_discovery(tweet_list)
	return jsonify({}),200

@app.route('/friends_and_interests/<handle>/<location>', methods=['GET','POST'])
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

if __name__ == '__main__':
	app.run(port=5000)
