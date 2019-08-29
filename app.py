from flask import Flask, jsonify

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/user/<twitter_handle')
def user(twitter_handle):
	if twitter_handle == 'samlerner':
		return jsonify({
			'user_id': '1234',
			'name': 'Sam Lerner',
			'bio': 'OSU Computer Science. A in 5914',
			'avatar': 'test_avatar.jpg',
		})
	elif twitter_handle == 'bobbyj':
		return jsonify({
			'user_id': '2345',
			'name': 'Bobby Johnson',
			'bio': 'A generic name',
			'avatar': 'test_avatar2.jpg',
		})
	elif twitter_handle == 'JD':
		return jsonify({
			'user_id': '3456',
			'name': 'John Doe',
			'bio': 'An even more generic name',
			'avatar': 'test_avatar3.jpg',
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
		'samlerner',
		'bobbyj',
		'JD'
	])
