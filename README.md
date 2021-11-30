# WEBC

A simple web calculator written in Python. Using this application you can:

1. Create calculators
2. Create operations
3. Execute operations
4. Everything is logged

# Requirements

1. Python 3
2. Django 3
3. Sqlite3
4. pipenv 2021

# Development environment

Create virtual environment and/or install required packages:

    pipenv install

Check for configuration errors:

    pipenv run python3 manage.py check

Apply all migrations:

    pipenv run python3 manage.py migrate

Run tests

    pipenv run python3 manage.py test

Start a local development server:

    pipenv run python3 manage.py runserver

It will be available at http://localhost:8000