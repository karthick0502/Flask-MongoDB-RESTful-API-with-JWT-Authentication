from spiceblue import db, app
from flask import request, jsonify, Response, session, make_response
from flask_httpauth import HTTPTokenAuth
from spiceblue import bcrypt
from functools import wraps
import datetime
import json
import jwt
import uuid

# create collections

user_collection = db.users
template_collection = db.templates


def register_user():
    user = {'_id': uuid.uuid4().hex,
            'Headers': {'Accept': request.headers['Accept'],
                        'Content-Type': request.headers['Content-Type']
                        },
            'Body': {'firstname': request.json['firstname'],
                     'lastname': request.json['lastname'],
                     'email': request.json['email'],
                     'password': bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
                     }
            }
    # check existing user in db
    for data in user_collection.find():
        if user['Body']['email'] in data['Body']['email']:
            return jsonify('this mail is already registered'), 400

    if user_collection.insert_one(user):
        return jsonify(user), 200
    return jsonify('user is not registered'), 400


def login_user():
    auth = request.authorization
    if not auth.username and not auth.password:
        return jsonify('could not verify!'), 400
    user = db.users.find_one({'Body.email': auth.username})
    if not user:
        return jsonify('Incorrect Username and Password'), 400
    if bcrypt.check_password_hash(user['Body']['password'], auth.password):
        message = {'email': user['Body']['email'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
        sign_key = app.config['SECRET_KEY']
        token = jwt.encode(message, sign_key)
        return jsonify({'message': 'login successfully', 'token': token})
    return jsonify('Incorrect Password'), 400


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if request.headers.get('Authorization') is None:
            return jsonify('Please put the token to access templates')
        token = request.headers.get('Authorization')
        return func(token, *args, **kwargs)

    return decorated


def add_template(token):
    template = {'_id': uuid.uuid4().hex,
                'Headers': {'Authorization': token,
                            'Accept': request.headers['Accept'],
                            'Content-Type': request.headers['Content-Type']
                            },
                'Body':
                    {'template_name': request.json['template_name'],
                     'subject': request.json['subject'],
                     'body': request.json['body']
                     }
                }
    if template_collection.insert(template):
        return jsonify('template insert successfully'), 200
    return jsonify('templates is not added'), 400


def get_all_template(token):
    data = list(db.templates.find({'Headers.Authorization': token}))
    if data:
        return jsonify(data), 200
    return jsonify('Something Wrong!'), 400


def get_single_template(token, idx):
    data = db.templates.find_one({'Headers.Authorization': token, '_id': idx})
    if data:
        return jsonify(data), 200
    return jsonify('Invalid id'), 400


def update_template(token, idx):
    response = db.templates.update_one(
        {'Headers.Authorization': token, '_id': idx}, {'$set': {'Body.template_name': request.json['template_name'],
                                                                'Body.subject': request.json['subject'],
                                                                'Body.body': request.json['body']}
                                                       })
    if response.modified_count == 1:
        return jsonify('template was updated successfully'), 200
    else:
        return jsonify('This information already updated. Do more changes and try again'), 400


def delete_template(token, idx):
    response = db.templates.delete_one({'Headers.Authorization': token, '_id': idx})
    if response.deleted_count == 1:
        return jsonify({'message': 'template was deleted successfully', 'id': f'{idx}'}), 200
    else:
        return jsonify('It is already deleted. No more template exists by this id'), 400





'''
def summa():
    if request.headers.get('Authorization') is None:
        return jsonify('Please put the token to access templates')
    bearer = request.headers.get('Authorization')
    bearer_token = bearer
    token = bearer_token.split()[1]
    print(token)
    if token:
        data = jwt.decode(token, app.config['SECRET_KEY'], 'HS256')
        current_user = user_collection.find_one({'Body.email': data['email']})
        print(current_user)
    return jsonify('something wrong')
'''
