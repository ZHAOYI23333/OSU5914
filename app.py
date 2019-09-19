from flask import Flask, jsonify, request
from match_interests import get_most_alike_to_user
from tweet_api_src.get_interests_dict_from_disco import get_interests_from_discovery

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/user/<handle>')
def user(handle):
	if handle == '@mdo':
		return jsonify({ 'first': 'Mark', 'last': 'Otto', 'handle': '@mdo' }), 200
	if handle == '@fat':
		return jsonify({ 'first': 'Jacob', 'last': 'Thornton', 'handle': '@fat' }), 200
	if handle == '@twitter':
		return jsonify({ 'first': 'Larry', 'last': 'the Bird', 'handle': '@twitter' }), 200

	return 404

@app.route('/friends_and_interests/<handle>/<location>')
def friends_and_interests(handle, location):
	all_users = get_interests_from_discovery()
	most_alike_users = get_most_alike_to_user(handle, all_users)
	return jsonify({
		'friends': most_alike_users,
		'interests': all_users[handle]
	}), 200

if __name__ == '__main__':
	app.run(port=5000)
