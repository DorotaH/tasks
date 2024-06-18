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
 venv\Script\activate # on Linux source venv/bin/activate
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

# API documentation <a id='API'></a>
### Testing authentication
```bash
curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'
```

