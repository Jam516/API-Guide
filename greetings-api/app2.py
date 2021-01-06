from flask import Flask, request, jsonify
from flask_cors import CORS

data = [['English','Hello'],['Spanish','Hola'],['Italian','Cho'],['Turkish','Merhaba'],['German','Hallo']]

def create_app(test_config=None):
    app = Flask(__name__)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,POST,PATCH,OPTIONS')
        return response

    @app.route('/greetings')
    def greetings():
        return jsonify(data)

    @app.route('/greetings/<int:g_id>')
    def retrieve_greetings(g_id):
        return jsonify(data[g_id][1])

    @app.route('/greetings/<int:g_id>', methods=['PATCH'])
    def update_greetings(g_id):
        body = request.get_json()
        data[g_id][1] = body.get('greeting')

        return jsonify({
                  'success': True,
                  'language': body.get('language'),
                  'greeting': body.get('greeting')
              })

    @app.route('/greetings', methods=['POST'])
    def create_greetings():
        body = request.get_json()
        data.append([body.get('language'),body.get('greeting')])
        # print(body.get('language'))

        return jsonify({
                  'success': True,
                  'language': body.get('language'),
                  'greeting': body.get('greeting')
              })


    return app
