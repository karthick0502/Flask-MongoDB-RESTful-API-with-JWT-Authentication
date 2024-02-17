# models.py - Defines functions for user authentication and template management

# Importing necessary modules
from spiceblue import db, app
from flask import request, jsonify
from flask_httpauth import HTTPTokenAuth
from spiceblue import bcrypt
from functools import wraps
import datetime
import json
import jwt
import uuid

# MongoDB collections
user_collection = db.users
template_collection = db.templates

# Function to register a new user
def register_user():
    # Creating user document
    user = {
        '_id': uuid.uuid4().hex,
        'Headers': {
            'Accept': request.headers['Accept'],
            'Content-Type': request.headers['Content-Type']
        },
        'Body': {
            'firstname': request.json['firstname'],
            'lastname': request.json['lastname'],
            'email': request.json['email'],
            'password': bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
        }
    }

    # Check if user already exists
    for data in user_collection.find():
        if user['Body']['email'] in data['Body']['email']:
            return jsonify('This email is already registered'), 400

    # Insert user into the database
    if user_collection.insert_one(user):
        return jsonify(user), 200
    return jsonify('User is not registered'), 400

# Function to authenticate and login a user
def login_user():
    auth = request.authorization
    if not auth.username and not auth.password:
        return jsonify('Could not verify!'), 400
    user = db.users.find_one({'Body.email': auth.username})
    if not user:
        return jsonify('Incorrect Username and Password'), 400
    if bcrypt.check_password_hash(user['Body']['password'], auth.password):
        message = {'email': user['Body']['email'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
        sign_key = app.config['SECRET_KEY']
        token = jwt.encode(message, sign_key)
        return jsonify({'message': 'Login successful', 'token': token})
    return jsonify('Incorrect Password'), 400

# Decorator function to check for token in requests
def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        if request.headers.get('Authorization') is None:
            return jsonify('Please provide a token to access templates')
        token = request.headers.get('Authorization')
        return func(token, *args, **kwargs)
    return decorated

# Function to add a new template
def add_template(token):
    template = {
        '_id': uuid.uuid4().hex,
        'Headers': {
            'Authorization': token,
            'Accept': request.headers['Accept'],
            'Content-Type': request.headers['Content-Type']
        },
        'Body': {
            'template_name': request.json['template_name'],
            'subject': request.json['subject'],
            'body': request.json['body']
        }
    }
    if template_collection.insert(template):
        return jsonify('Template inserted successfully'), 200
    return jsonify('Template was not added'), 400

# Function to retrieve all templates
def get_all_template(token):
    data = list(db.templates.find({'Headers.Authorization': token}))
    if data:
        return jsonify(data), 200
    return jsonify('Something went wrong!'), 400

# Function to retrieve a single template by ID
def get_single_template(token, idx):
    data = db.templates.find_one({'Headers.Authorization': token, '_id': idx})
    if data:
        return jsonify(data), 200
    return jsonify('Invalid ID'), 400

# Function to update a template
def update_template(token, idx):
    response = db.templates.update_one(
        {'Headers.Authorization': token, '_id': idx},
        {'$set': {
            'Body.template_name': request.json['template_name'],
            'Body.subject': request.json['subject'],
            'Body.body': request.json['body']
        }}
    )
    if response.modified_count == 1:
        return jsonify('Template was updated successfully'), 200
    else:
        return jsonify('This information is already updated. Make more changes and try again'), 400

# Function to delete a template
def delete_template(token, idx):
    response = db.templates.delete_one({'Headers.Authorization': token, '_id': idx})
    if response.deleted_count == 1:
        return jsonify({'message': 'Template was deleted successfully', 'id': f'{idx}'}), 200
    else:
        return jsonify('The template with this ID does not exist or has already been deleted'), 400
