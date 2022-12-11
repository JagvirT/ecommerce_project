from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password= db.Column(db.String(250), nullable=False)
    # post= db.relationship('Post', backref='Author', lazy=True)

    def __int__(self, username, email, password):
        self.username= username
        self.email= email
        self.password = password

    
# class Post(db.model):

