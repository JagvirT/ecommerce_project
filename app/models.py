from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin 
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

Cart = db.Table(
    'Cart',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable = False),
    db.Column('product_id', db.Integer, db.ForeignKey('product.id'), nullable= False)
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password= db.Column(db.String(250), nullable=False)
    # user_product= db.relationship('Product', backref='Author', lazy=True)
    get_product= db.relationship('Product', secondary= Cart,
        # primaryjoin= (Cart.columns.user_id== id),
        # secondaryjoin= (Cart.columns.product_id== id),
        backref = db.backref('Carts', lazy='dynamic'),
        lazy='dynamic'
    )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    
    def is_active(self):
       return True

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def add_product(self, product):
        self.get_product.append(product)
        db.session.commit()
    
    def delete_product(self, product):
        self.get_product.remove(product)
        db.session.commit()



# class Cart(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

#     def __init__(self, product_id, user_id):
#         self.product_id = product_id
#         self.user_id = user_id

    
#     def save_to_db(self):
#         db.session.add(self)
#         db.session.commit()
    


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    # order = db.relationship(Cart, backref="order", lazy=True)

    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


# class Info(db.model):
#     id = db.Column(db.Integer, primary_key= True)


    # cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)

