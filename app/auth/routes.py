from flask import Blueprint, render_template
from app.auth.forms import UserCreationForm
auth = Blueprint('auth', __name__, template_folder="auth templates")

@auth.route('/signup')
def signup():
    form = UserCreationForm()
    return render_template('signup.html', form=form)


@auth.route('/login')
def login():
    return render_template('login.html')