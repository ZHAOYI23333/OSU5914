from flask import Flask, jsonify, request

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

@app.route('/interests/<handle>')
def interests(handle):
	if handle == "@slerner":
		return jsonify(["Basketball", "Soccer", "Drawing", "Painting", "Archery", "Swimming"]), 200
	elif handle == "@mdo":
		return jsonify(["Basketball", "Soccer"]), 200
	elif handle == "@fat":
		return jsonify(["Drawing", "Soccer"]), 200
	elif handle == "@twitter":
		return jsonify(["Archery", "Painting", "Swimming"]), 200

	return 404

@app.route('/similar_users/<location>')
def friends(location):
	interests = request.args.get('interests').split(',')

	return jsonify([
		'@mdo',
		'@fat',
		'@twitter'
	]), 200

if __name__ == '__main__':
	app.run(port=5000)
