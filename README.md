# Online web-service «Evrika – mentoring»
![https://www.djangoproject.com/download/](https://img.shields.io/badge/Django-3.2.15-1AC650)
![https://ru.vuejs.org/v2/guide/installation.html](https://img.shields.io/badge/Vue-2.7.8-1AC650)

It is a modern online web-service is designed for search and placement projects which related to «Evrika». «Evrika» is an association that helps students take part in writing scientific research works. Project working on 3 applications: Vue/CLI, Django/DRF and PostgreSQL. The client-side and server-side are connected using Axios (at frontend) and Django REST framework (at backend).


### About project
The project based on client-server architecture. Project's structure:
- <strong>/frontend</strong> Front-end side folder which using Vue/CLI. Detailed description of styles and components you can see at here;
- <strong>/backend</strong> Back-end side folder which using Django with Django REST framework. Must be using only for responses to requests from front-end side or site management;
<br/><br/>


## Getting started
This is guide to getting a copy of this project for local development or testing some features. Before installing the project, you need to have git on your computer. 
Copying the project:
```bash
git clone git@github.com:denis-vyzulin/evrika-mentoring.git
cd evrika-mentoring
```

When project is copied, you need to setting up project. There are two ways to do this:
1. [Setting up project via docker](#setting-up-project-via-docker) (prefer)
2. [Setting up project without docker](#setting-up-project-without-docker)
<br><br>


### Setting up project via docker
Run local version for development or testing like this:
```bash
# Run this from root directory
docker-compose -f docker-compose.dev.yml up -d --build
```
###### After this command, the project should be successfully running
<br>


### Setting up project without docker
Setting up <b>Backend</b> side (cd the /backend folder, before starting). Install required version of python (3.6 – 3.10). Then create virtual environment and install dependencies:
```bash
cd ./backend

pip install virtualenv
python -m virtualenv venv
source venv/scripts/activate

pip install -r requirements.txt

python manage.py runserver --settings=config.settings.dev
```
###### Backend side should be successfully running
<br>

Setting up <b>Frontend</b> side (cd the /frontend folder, before starting). Before starting install npm (higher then 6.0.0) and vue with cli (higher than 3.0.0).
```bash
cd ./frontend

npm install
npm run serve
```
###### Frontend side should be successfully running
