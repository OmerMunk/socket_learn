from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import User
from app.forms import LoginForm
from flask_login import login_user, logout_user, login_required

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('welcome'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)

@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))



