from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from app.auth.forms import UserCreationForm, LoginForm
from app.models import User, Product, db, Cart
from werkzeug.security import check_password_hash

auth = Blueprint('auth', __name__, template_folder="auth templates")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            username= form.username.data
            email= form.email.data
            password= form.password.data


            user = User(username, email, password)

            user.save_to_db()
            return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)


@auth.route('/login', methods= ['GET', 'POST'])
def login():
    form= LoginForm()
    if request.method== 'POST':
        if form.validate():
            username =form.username.data
            password = form.password.data

            user = User.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    print("logged in")
                    login_user(user)
                else:
                    ('Invalid password')
            else:
                print('User does not exist')


    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/available_products')
def available_products():
    products = Product.query.all()
    return render_template('available_products.html', products=products[::-1])

@auth.route('/available_products/<int:product_id>')
def this_product(product_id):
    product = Product.query.get(product_id)
    if product:
        return render_template('this_product.html', product=product)
    else:
        return redirect(url_for('auth.available_products'))

@auth.route('/your_cart/<int:product_id>')
def your_cart(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if product:
        current_user.add_product(product)
    
    my_cart = current_user.get_product.all()
    print(my_cart)
    total= 0
    for item in my_cart:
        total += item.price


    return render_template('your_cart.html',  cart= my_cart, total=total)


@auth.route('/your_cart/delete/<int:product_id>')
def remove_item(product_id):
    product = Product.query.filter_by(id=product_id).first()
    if product:
        current_user.delete_product(product)

    # item = Product.query.get(product_id)
    # if item:
    #     db.session.delete(item)
    #     db.session.commit()
    return redirect(url_for('auth.your_cart'))

