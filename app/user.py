from flask import (Flask, Blueprint, flash, g, redirect, url_for, render_template)

bp = Blueprint('user', __name__)

@bp.route('/')
def index():
    return render_template('index.html')