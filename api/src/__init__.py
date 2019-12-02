from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import UserMixin, LoginManager, current_user, login_user, logout_user, login_required

app = Flask(__name__)
# CORS(app)
app.config.from_object('config.Config')

db = SQLAlchemy(app)

## import Models
from src.models.user import User
migrate = Migrate(app, db)

## set up Login_manager
login_manager = LoginManager()
login_manager.init_app(app)
# login_manager.login_view = "userpd.login"

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)
