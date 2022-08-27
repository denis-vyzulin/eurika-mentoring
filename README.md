# Mentoring web-service «Evrika»
![https://www.djangoproject.com/download/](https://img.shields.io/badge/Django-3.2.15-1AC650)
![https://ru.vuejs.org/v2/guide/installation.html](https://img.shields.io/badge/Vue-2.7.8-1AC650)

It is a comfortable service for searching projects related to «Evrika». Evrika is a scientific society of Nizhny Novgorod students,
which working based on DDT Chkalova since 1969.
<br><br>


## Getting started
Guide to getting a copy of the project for local development or testing some feature. Before installing the project, you need to have git on your computer.

### Project requirements
| Requirement | Required Versions |
| :---- | :--- |
| [Python](https://www.python.org/downloads/) | 3.6, 3.7, 3.8, 3.9, 3.10 |
| [Node.js](https://nodejs.org/en/download/) | higher than 6.0.0 |
| [npm](https://nodejs.org/en/download/) | higher than 3.0.0 |
###### Click on the name of the requirement program for go to the installation website
<br>


## Setting up project
1. First, you need to install project files and all dependencies
```bash
# Clone project from github repository
$ git clone git@github.com:dintear/evrika-mentoring.git evrika-mentoring
$ cd evrika-mentoring

# Install backend dependencies 
$ python -m venv venv
$ source venv/bin/activate
$ python -m pip install -r requirements.txt

# Install frontend dependencies
$ cd frontend
$ npm install
```
2. After installation all dependecies, you can run frontend and backend server
```bash
# Run backend server
$ cd ../backend
$ python manage.py runserver

# Run frontend server
$ cd ../frontend
$ npm run dev
```
###### Now, your project ready for development