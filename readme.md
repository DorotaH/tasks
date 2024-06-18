# Tasks application
## Description
This is a simple web application built for learning purposes. It uses the Django Rest Framework (DRF) for the backend, and Docker, Gunicorn, and Nginx for deployment. The application allows users to register, log in, and manage simple tasks </br>
### How to
- [Start an application](#ap)
- [Run tests](#tests)
- [Format code](#formatCode)
- [API documentation](#API)
<a id='app'></a>
# How to start an application
### 1. Create a virtual environment 
Although venv is not needed it is highly recommended. To create and run it use:
```bash
 python -m venv venv
 source venv/bin/activate # on Windows venv\Script\activate 
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run docker 
```bash
 docker-compose up # -d flag for running app in the background
```
how does it work? Docker automates the deployment process, enabling us to launch an application with a single command. Gunicorn, on the other hand, creates multiple worker processes to manage incoming requests. Meanwhile, Nginx is responsible for handling static files.

<a id='tests'></a>
# Running tests
```bash
pytest
```

<a id='formatCode'> </a>
# Formatting your code 
```bash
ruff format
```
<a id='API'></a>
# API documentation 
## Tasks Endpoints
curl is command-line tool used to transfer data to or from a server,
- The -X option specifies the request method to use (e.g., POST, PUT, DELETE, etc.), with GET being the default method,
- The URL specifies where we want the request to be sent,
- The -H option allows for adding headers. In this case, we are adding the Authorization header as we need to be logged in to be able to access tasks,
- The -d option sends specific information in the request body, with the data being URL-encoded,
- *To filter tasks, we need to change the URL to include the parameters we want to search for.
### get all tasks
```bash
 curl http://127.0.0.1:8000/tasks/ -H 'Authorization: Basic example_token'
```
### get tasks with params
```bash
 curl http://127.0.0.1:8000/tasks/?search=example&status=N&name=name -H 'Authorization: Basic example_token
```
### create task
```bash
 curl -X POST http://127.0.0.1:8000/tasks/ -H "Authorization: Basic example_token" -d "name=NewTask&description=Taskdescription&status=P&user=1"
```
### get task by id
```bash
 curl http://127.0.0.1:8000/tasks/1/ -H "Authorization: Basic example_token"
```
### modify a task by id
```bash
 curl -X PUT http://127.0.0.1:8000/tasks/1/ -H "Authorization: Basic example_token" -d "name=newName&description=newDescription&status=C&user=1"
```
### Delete a task by id
```bash
 curl -X DELETE http://127.0.0.1:8000/tasks/1/ -H "Authorization: Basic example_token" 
```
