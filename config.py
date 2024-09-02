#!/usr/bin/env python3
"""
Handles database configuration and loads all env variables needed
"""

from os import getenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from flask_mail import Mail

load_dotenv()

user = getenv("USER")
database = getenv("DB")
password = getenv("PWD")
host = getenv("HOST")
key = getenv("KEY")
print(user, database, password, host, key)

# Initialize the flask app
app = Flask(__name__)
# csrf = CSRFProtect(app)
# CORS(app, resources={r"/*": {"origins": "http://localhost:5000"}})

# Configure the email server settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = getenv('EMAIL_PORT')
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = getenv('APP_MAIL')
app.config['MAIL_PASSWORD'] = getenv('APP_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = (getenv('USERNAME'), getenv('APP_MAIL'))

mail = Mail(app)

app.config['SECRET_KEY'] = key

if app.config['TESTING']:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
else:
    app.config['SQLALCHEMY_DATABASE_URI']\
        = f'mysql+mysqldb://{user}:{password}@{host}/{database}'

db = SQLAlchemy(app)

migrate = Migrate(app, db)


