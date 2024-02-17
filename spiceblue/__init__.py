# __init__.py - Initialization file for the Flask application

# Importing necessary modules from Flask
from flask import Flask
from flask_pymongo import pymongo
from flask_bcrypt import Bcrypt

# Creating the Flask application instance
app = Flask(__name__)

# Initializing Bcrypt for password hashing
bcrypt = Bcrypt(app)

# Setting up a secret key for session security
app.config['SECRET_KEY'] = 'e4b3a928dc944375bd2747b224357307'

# Connecting to MongoDB database
client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.2figo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.spiceblue

# Importing routes after initializing the Flask application instance
from spiceblue import routes
