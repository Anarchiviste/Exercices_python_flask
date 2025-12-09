from flask import Flask
from flask import request
from flask import url_for
from flask import render_template #pour les templates


app = Flask(
	__name__,
	template_folder='templates',
    static_folder='statics'
)


'''class Base(DeclarativeBase):
    pass

db = SQLAlchemy(app)'''

from .route import generales