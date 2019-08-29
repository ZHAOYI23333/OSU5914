from flask import Flask, jsonify

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/user/<twitter_handle>')
def user(twitter_handle):
	if twitter_handle == 'samlerner':
		return jsonify({
			'name': 'Sam Lerner',
			'bio': 'OSU Computer Science. A in 5914',
			'avatar': 'test_avatar.jpg',
		})
	elif twitter_handle == 'bobbyj':
		return jsonify({
			'name': 'Bobby Johnson',
			'bio': 'A generic name',
			'avatar': 'test_avatar2.jpg',
		})
	elif twitter_handle == 'JD':
		return jsonify({
			'name': 'John Doe',
			'bio': 'An even more generic name',
			'avatar': 'test_avatar3.jpg',
		})

@app.route('/interests/<twitter_handle>')
def interests(twitter_handle):
	return jsonify([
		'baseketball',
		'poetry',
		'music',
		'heavy metal',
		'computer science'
	])

@app.route('/friends/<twitter_handle>')
def friends(twitter_handle):
	return jsonify([
		'samlerner',
		'bobbyj',
		'JD'
	])

if __name__ == '__main__':
	app.run(port=5000)
