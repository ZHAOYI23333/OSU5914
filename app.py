from flask import Flask, jsonify, request
from match_interests import get_most_alike_to_user

import os
from os.path import join
import sys
sys.path.insert(0, join(os.getcwd(), 'tweet_api_src'))
sys.path.insert(0, join(os.getcwd(), 'geo_service_src'))

from geocode import get_coordinate
from get_interests_dict_from_disco import get_interests_from_discovery
from upload_all_user_tweets_to_discovery import upload_tweets_to_discovery
from tweet_handler import get_tweets_by_location, get_tweets_by_user, get_users_by_tweets, upload_all_tweets_of_users
from disco_utils import *
import json

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/user/<handle>', methods=['GET','POST'])
def user(handle):
	location_query = request.args.get('location')
	location = ','.join(list(reversed([str(l) for l in get_coordinate(location_query)]))) + ',50km'

	tweets = get_tweets_by_location(location)
	users = list(get_users_by_tweets(tweets))
	users = users[:min(len(users), 3)]
	upload_all_tweets_of_users(users, location_query)

	tweet_list = get_tweets_by_user(handle)
	upload_tweets_to_discovery(tweet_list, location_query)
	return jsonify({}), 200

@app.route('/friends_and_interests/<handle>/<location>', methods=['GET','POST'])
def friends_and_interests(handle, location):
	users_in_region = get_interests_from_discovery(location, handle)
	most_alike_users = get_most_alike_to_user(handle, users_in_region)

	interests = []

	if handle in users_in_region:
		interests = users_in_region[handle]
		
	return jsonify({
		'friends': most_alike_users,
		'interests': interests
	}), 200

if __name__ == '__main__':
	app.run(port=5000)
