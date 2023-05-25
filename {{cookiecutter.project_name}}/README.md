# {{ cookiecutter.project_name }} Django Application

## Pre-requirements

Before getting started with the project, it is essential to ensure that you have the following pre-requisites installed and set up on your development environment:

1. **Git**: Make sure you have Git installed on your system. Git is a distributed version control system that allows you to track changes to your project's codebase. You can download and install Git from the official website [here](https://git-scm.com/) or use a package manager specific to your operating system.

2. **Python**: The project is based on Django - Python web framework, so you'll need to have Python installed on your machine. Project works with Python versions 3.10 or higher. You can download the latest version of Python from the official Python website [here](https://www.python.org/downloads/). Make sure to choose the version compatible with your operating system.


## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/example/{{ cookiecutter.project_name }}.git
$ cd {{ cookiecutter.project_name }}
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements/local.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by us

Once `pip` has finished downloading the dependencies fill the .env file with appropriate values,
apply the migrations and run the development server:
```sh
(env)$ python manage.py migarate
(env)$ python manage.py runserver
```

The project supports and containerization:
```sh
(env)$ docker-compose up --build
```

And navigate to `http://127.0.0.1:8000/`.

## Django Skeleton Project

```bash
root
├── apps
│   ├── core
│   │   ├── apps.py
│   │   ├── constants.py
│   │   ├── helpers.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── urls.py
│   ├── example_api
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── v1
│   │   │   │   ├── __init__.py
│   │   │   │   ├── serializers.py
│   │   │   │   ├── services.py
│   │   │   │   ├── tests.py
│   │   │   │   ├── urls.py
│   │   │   │   └── views.py
│   │   │   └── v2
│   │   │       ├── __init__.py
│   │   │       ├── serializers.py
│   │   │       ├── services.py
│   │   │       ├── tests.py
│   │   │       ├── urls.py
│   │   │       └── views.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── management
│   │   │   ├── commands
│   │   │   │   ├── command.py
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── utils.py
│   └── __init__.py
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings
│   │   ├── base.py
│   │   ├── __init__.py
│   │   ├── local.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── db
├── docker
│   ├── local
│   │   └── Dockerfile
│   ├── docker-compose.yaml
│   └── prod
├── docs
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── deployment.md
│   ├── local-development.md
│   └── swagger.yaml
├── entrypoint.sh
├── manage.py
├── media
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements
│   ├── base.txt
│   ├── development.txt
│   ├── local.txt
│   └── production.txt
└── static
```