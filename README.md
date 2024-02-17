# Title: Flask-MongoDB RESTful API with JWT Authentication

## Description:
This project implements a RESTful API using Flask and MongoDB, incorporating JWT access token-based authentication for user management. It allows users to register, login, and perform CRUD operations on templates, with access control restrictions ensuring each user can only manipulate their own templates.

## Installation:
1. Install Flask: `pip install Flask`
2. MongoDB: Register and host the MongoDB database files at [MongoDB Atlas](https://account.mongodb.com/account/register).

## Technologies:
The technologies used in this project include:

1. **Flask**: Flask is a lightweight WSGI web application framework in Python. It's used here to create the RESTful API endpoints and handle HTTP requests.

2. **MongoDB**: MongoDB is a NoSQL database used for storing data in a document-oriented format. It's utilized in this project to persistently store user information and templates.

3. **JWT (JSON Web Tokens)**: JWT is a compact, URL-safe means of representing claims to be transferred between two parties. It's employed here for authentication purposes, providing access tokens for secure communication between the client and the server.

4. **Postman**: Postman is a collaboration platform for API development. While not a technology per se, it's mentioned in the project description as the tool used for testing the API endpoints.

5. **Flask-PyMongo**: Flask-PyMongo is a Flask extension that simplifies the interaction between Flask applications and MongoDB databases. It's used here to facilitate database operations within the Flask application.

6. **Flask-Bcrypt**: Flask-Bcrypt is another Flask extension used for password hashing. It's employed here to securely hash passwords before storing them in the database.

7. **Python**: Python is the primary programming language used for developing the Flask application and defining the API endpoints, as well as handling various backend operations.

These technologies collectively enable the creation of a robust and secure RESTful API with user authentication and CRUD operations on templates stored in a MongoDB database.

## Usage:
1.Register
    
    URL : localhost:5000/register
    Method : POST
    Headers : {
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                first_name : 'lead_test@subi.com',
                last_name : '123456'
                email : 'lead_test@subi.com',
                password : '123456'
              }


2.Login

    URL : localhost:5000/login
    Method : POST
    Headers : {
                 'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                email : 'lead_test@subi.com',
                password : '123456'
              }  

    
3.Template CRUD
    
    1.Insert new Template

    URL : locahost:5000/template

    Method : POST
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                'template_name': ' ',
                'subject': ' ',
                'body': ' ',
                     }  

    2.Get All Template

    URL : locahost:5000/template
    
    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}      


    3.GET Single Template

    URL : locahost:5000/template/<template_id>

    Method : GET
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}  

    2.Update Single Template

    URL : locahost:5000/template/<template_id>
    
    Method : PUT
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {
                'template_name': ' ',
                'subject': ' ',
                'body': ' ',
    }   

    3.DELETE Single Template

    URL : locahost:5000/template/<template_id>

    Method : DEL
    Headers : {
                'Authorization': 'Bearer ' + <access_token from login step>,
                'Accept': 'application/json',
                'Content-Type': 'application/json',          
              }
    Body :    {}                  


