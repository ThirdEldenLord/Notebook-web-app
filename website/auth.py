from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import data_base
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

#Login function
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.notes'))
            else:
                flash('Password incorrect', category='error')
        else:
            flash('Account does not exist', category='error')    
        
    return render_template("login.html", user=current_user)

#Logout function
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

#Sign up function
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        email = request.form.get('email')
        password_1 = request.form.get('password_1')
        password_2 =request.form.get('password_2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Account already exist', category='error')
        elif len(first_name) < 3:
            flash('First name should be atleast 3 characters', category='error')
        elif len(email) < 5:
            flash('Email should be atleast 5 characters', category='error')
        elif password_1 != password_2:
            flash('Passwords do not match', category='error')
        elif len(password_1) < 5:
            flash('Password should be atleast 5 characters', category='error')
        else:
            new_user = User(first_name=first_name, email=email, password=generate_password_hash(password_1, method='pbkdf2:sha256'))
            data_base.session.add(new_user)
            data_base.session.commit()
            login_user(new_user, remember=True)
            flash('Your account successfully created', category='success')
            return redirect(url_for('views.notes'))
            
    return render_template("sign_up.html", user=current_user)
    