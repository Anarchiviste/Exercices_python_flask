from flask import Flask
from flask import request
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__, template_folder="templates", static_folder="statics")

version_variable = "0.0.1"
"""class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app)"""

from .route import generale
