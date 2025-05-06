from flask import (Flask, Blueprint, flash, g, redirect, url_for, render_template)
from app.auth import login_required

bp = Blueprint('user', __name__)

@bp.route('/')
def index():
    return render_template('user/index.html')


@bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('user/dashboard.html')

@bp.route('/profile')
@login_required
def profile():
    return render_template('user/profile.html')