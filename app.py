from flask import Flask, jsonify

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/user/<handle>')
def user(handle):
	if handle == '@mdo':
		return jsonify({ 'first': 'Mark', 'last': 'Otto', 'handle': '@mdo' })
	if handle == '@fat':
		return jsonify({ 'first': 'Jacob', 'last': 'Thornton', 'handle': '@fat' })
	if handle == '@twitter':
		return jsonify({ 'first': 'Larry', 'last': 'the Bird', 'handle': '@twitter' })

@app.route('/interests/<handle>')
def interests(handle):
	if handle == "@slerner":
		return jsonify(["Basketball", "Soccer", "Drawing", "Painting", "Archery", "Swimming"])
	elif handle == "@mdo":
		return jsonify(["Basketball", "Soccer"])
	elif handle == "@fat":
		return jsonify(["Drawing", "Soccer"])
	elif handle == "@twitter":
		return jsonify(["Archery", "Painting", "Swimming"])

@app.route('/friends/<handle>')
def friends(handle):
	return jsonify([
		'@mdo',
		'@fat',
		'@twitter'
	])

if __name__ == '__main__':
	app.run(port=5000)
