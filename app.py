from flask import Flask, jsonify

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/user/<twitter_handle')
def user(twitter_handle):
	return jsonify({
		'user_id': '1234',
		'name': 'Sam Lerner',
		'bio': 'OSU Computer Science. A in 5914',
		'avatar': 'test_avatar.jpg',
	})

@app.route('/interests/<user_id>')
def interests(user_id):
	return jsonify([
		'baseketball',
		'poetry',
		'music',
		'heavy metal',
		'computer science'
	])

@app.route('/friends/<user_id>')
def friends(user_id):
	return jsonify([
		'Sam Lerner',
		'Bobby Johnson',
		'John Doe'
	])
