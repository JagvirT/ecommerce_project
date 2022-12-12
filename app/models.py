from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin 

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password= db.Column(db.String(250), nullable=False)
    user_product= db.relationship('Cart', backref='Author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def is_active(self):
       return True

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, product_id, name, price, quantity, user_id):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity
        self.user_id = user_id

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)   
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# class Info(db.model):
#     id = db.Column(db.Integer, primary_key= True)


    # cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)

