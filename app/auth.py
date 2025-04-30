import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        tel = request.form['tel']
        state = request.form['state']
        gender = request.form['gender']
        password = request.form['password']
        db = get_db()
        error = None

        if not firstname:
            error = 'First Name required!'
        elif not email:
            error = 'Email is required!'
        elif not password:
            error = 'password is required!'

        if error is None:
            try:
                db.execute("INSERT INTO user (firstname, lastname, email, tel, state, gender, password) VALUES (?, ?, ?, ?, ?, ?, ?)", (firstname, lastname, email, tel, state, gender, generate_password_hash(password)),)
                db.commit()
            except db.IntegrityError:
                error = f"{email} is already registered."
            else:
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        # Used get() to safely handle missing keys.
        email = request.form.get('email')
        password = request.form.get('password')
        db = get_db()
        error = None
        user = db.execute('SELECT * FROM user WHERE email = ?', (email,)).fetchone()
        # Check if user exists and password is valid
        if not user:
            error = 'Invalid Email or Password!' # General error for security reasons
        elif not check_password_hash(user['password'], password): # Verify hashed password
            error = 'Invalid Email or Password!' # Same error to avoid giving clues.

        if error is None:
            # clear session and log in user
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        # pass the error to flash for the user
        flash(error, "error")
    return render_template('auth/login.html', flash=flash)

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM user WHERE id = ?', (user_id,)).fetchone()

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
