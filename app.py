import flask

from flask import request, jsonify

welcomeMessage = { "messenger": "tejaswi", "message": "Hello! Stay Safe!!" }

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/hello', methods=['GET'])
def home():
    return jsonify(welcomeMessage)

app.run()
