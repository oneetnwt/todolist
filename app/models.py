from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    username = db.Column(db.String(150), primary_key=True)
    password = db.Column(db.String(150))