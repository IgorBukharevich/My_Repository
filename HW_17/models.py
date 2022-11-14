"""
Models and Table on create
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from appflask import db


class Users(db.Model):
    """Create table 'Users'"""
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    psw = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<users {self.id}>'


class Profiles(db.Model):
    """Create table 'Profiles'"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    city = db.Column(db.String(200), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<users {self.id}>'
