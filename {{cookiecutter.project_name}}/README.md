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
(env)$ docker compose up
```

And navigate to `http://127.0.0.1:8000/`.

## Running Project Tests

In the root folder of the project type:
```sh
(env)$ python manage.py test
```

To run the tests with coverage type:
```sh
(env)$ coverage run manage.py test
```

Once you have executed the tests with coverage, you can generate a coverage report:
```sh
(env)$ coverage report
```

For better understanding of the test coverage situation you can generate html report:
```sh
(env)$ coverage html
```

#### It's highly recommend striving for a test coverage of more than 80% in the project. 

## Linting, types checking, static security analysis

It's a good practice the linters, the type checkers and static analysis tools to be a part of the pre-commmit hook
but you can run them from the terminal as well.

```sh
(env)$ ruff .
```

```sh
(env)$ mypy .
```

```sh
(env)$ bandit -r ./apps
```

```sh
(env)$ pip-audit .
```


## Documentation

Swagger documentation is available: \
`http://127.0.0.1:8000/docs/swagger-ui/` \
`http://127.0.0.1:8000/docs/redoc/`
