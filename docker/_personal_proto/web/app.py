from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://my_db:27017")
db = client.projectDB
users = db['Users']

def userExist(username):
    if users.find({'Username': username}).count() == 0:
        return False
    else:
        return True

def verifyUser(username, password):
    if not userExist(username):
        return False

    user_hashed_pw = users.find({
        'Username': username
    })[0]['Password']

    if bcrypt.checkpw(password.encode('utf8'), user_hashed_pw):
        return True
    else:
        return False

def getUserMessages(username):
    return users.find({
        'Username': username
    })[0]['Messages']

class Hello(Resource):
    def get(self):
        return 'Hello World!'

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        if userExist(username):
            retJson = {
                'status': 301,
                'msg': 'Invalid Username'
            }
            return jsonify(retJson)
        
        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        users.insert({
            'Username': username,
            'Password': hashed_pw,
            'Messages': []
        })
        retJson = {
            'status': 200,
            'msg': 'Registration successful'
        }
        return jsonify(retJson)

class Retrieve(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']

        if not userExist(username):
            retJson = {
                'status': 301,
                'msg': 'Invalid Username'
            }
            return jsonify(retJson)

        correct_pw = verifyUser(username, password)
        if not correct_pw:
            retJson = {
                'status': 302,
                'msg': 'Invalid password'
            }
            return jsonify(retJson)

        messages = getUserMessages(username)
        retJson = {
            'status': 200,
            'obj': messages
        }
        return jsonify(retJson)

class Save(Resource):
    def post(self):
        data = request.get_json()
        username = data['username']
        password = data['password']
        message = data['message']

        if not userExist(username):
            retJson = {
                'status': 301,
                'msg': 'Invalid Username'
            }
            return(retJson)

        correct_pw = verifyUser(username, password)
        if not correct_pw:
            retJson = {
                'status': 302,
                'msg': 'Invalid password'
            }
            return jsonify(retJson)

        if not message:
            retJson = {
                'status': 303,
                'msg': 'Please supply  valid message'
            }
            return jsonify(retJson)

        messages = getUserMessages(username)
        messages.append(message)

        users.update({
            'Username': username
        }, {
            '$set': {
                'Messages': messages
            }
        })
        retJson = {
            'status': 200,
            'msg': 'Message saved successfully'
        }
        return jsonify(retJson)

api.add_resource(Hello, '/hello')
api.add_resource(Register, '/register')
api.add_resource(Retrieve, '/retrieve')
api.add_resource(Save, '/save')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

