"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)
# TODO: Add any logging levels and handlers with app.logger
app.logger.setLevel(logging.INFO)
log_file = "app.log"
file_handler = RotatingFileHandler(log_file, maxBytes=10240, backupCount=5)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] - %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
