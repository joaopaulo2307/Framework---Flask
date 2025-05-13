from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user
from werkzeug.security import check_password_hash
from ..models import User
from .. import db, login_manager
from .forms import LoginForm

auth_bp = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        flash('Usuário ou senha inválidos.')
    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))