from flask import Flask, jsonify
from flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,OPTIONS')
        return response

    @app.route('/')
    def greeting():
        return jsonify({'message': 'Hello'})

    @app.route('/spanish')
    def spanish_greeting():
        return 'Hola'

    return app
