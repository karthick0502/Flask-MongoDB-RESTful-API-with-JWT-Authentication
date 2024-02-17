from flask import Flask
from flask_pymongo import pymongo

from flask_bcrypt import Bcrypt


app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'e4b3a928dc944375bd2747b224357307'

# Create DataBase

client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.2figo.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.spiceblue

from spiceblue import routes

