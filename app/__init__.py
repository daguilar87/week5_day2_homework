from flask import Flask
from config import Config
from auth.routes import auth

app = Flask(__name__)

app.config.from_object(Config)

from . import routes

from .models import db, User
from flask_migrate import Migrate
from flask_login import LoginManager

login = LoginManager()

@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)

db.init_app(app)
migrate = Migrate(app, db)

login.init_app(app)
login.login_view = 'auth.loginPage'

app.register_blueprint(auth)