import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db
from app.utils import get_state, clean_name_input, is_valid_email, clean_phone_number

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        db = get_db()
        error = None
        firstname = clean_name_input(request.form.get('firstname'))
        lastname = clean_name_input(request.form.get('lastname'))
        email = request.form.get('email').strip().lower()

        if not is_valid_email(email):
            error = "Invalid email format!"

        tel = request.form.get('tel').strip()
        tel = clean_phone_number(tel)

        state = request.form.get('state_name')
        gender = request.form.get('gender')
        password = request.form.get('password').strip()
        re_type = request.form.get('retype').strip()


        if not firstname:
            error = 'First Name required!'
        elif not email:
            error = 'Email is required!'
        elif not state:
            error = 'Please select your state!'
        elif not gender:
            error = " select your gender!"
        elif not password:
            error = 'password is required!'
        elif not re_type:
            error = 'matching password is required!'
        elif re_type != password:
            error = 'password not match!'
        elif len(password) < 8:
            error = 'password must be atleast 8-char long!'

        if error is None:
            try:
                db.execute("INSERT INTO user (firstname, lastname, email, tel, state, gender, password) VALUES (?, ?, ?, ?, ?, ?, ?)", (firstname, lastname, email, tel, state, gender, generate_password_hash(password)),)
                db.commit()
            except db.IntegrityError:
                error = f"{email} is already registered."
            else:
                flash('Successfully created! You can now log in.', "success")
                print(state)
                return redirect(url_for("auth.login"))
        flash(error, "error")
    state = get_state()
    return render_template('auth/register.html', state=state)

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        # Used get() to safely handle missing keys.
        email = request.form.get('email').lower()
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
            return redirect(url_for('user.dashboard'))

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

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view