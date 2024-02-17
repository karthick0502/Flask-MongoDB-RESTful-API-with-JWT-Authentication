# Title: Flask-MongoDB RESTful API with JWT Authentication

## Description:
This project implements a RESTful API using Flask and MongoDB, incorporating JWT access token-based authentication for user management. It allows users to register, login, and perform CRUD operations on templates, with access control restrictions ensuring each user can only manipulate their own templates.

## Installation:
1. Install Flask: `pip install Flask`
2. MongoDB: Register and host the MongoDB database files at [MongoDB Atlas](https://account.mongodb.com/account/register).

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


2 Login

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

    
    2 Template CRUD
    
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


