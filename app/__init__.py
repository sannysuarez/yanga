import os
from flask import Flask, g, session
from app.db import get_db

def create_app(test_config=None):
    # Create and configure the App
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'app.sqlite'),)

    app.config["UPLOAD_EXTENSIONS"]=[".xlsx", ".xls", ".pdf"]
    app.config["UPLOAD_PATH"]="app/static/profile_pictures/"

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config is passed in
        app.config.from_mapping(test_config)

        # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import user
    app.register_blueprint(user.bp)
    app.add_url_rule('/', endpoint='index')

    return app


