import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.controller import users

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.register_blueprint(users, url_prefix='/users')
