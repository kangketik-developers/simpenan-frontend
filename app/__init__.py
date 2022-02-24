import os

from flask import Flask

from .controllers import auth
from .controllers import dashboard
from .controllers import users
from .controllers import inmates
from .controllers import attendances
from .controllers import reports

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="1a13bf4224e28f934efcbb85701137db094c3889bdff16c958aa73e29656c2c1"
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # db.init_app(app)

    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(users.bp)
    app.register_blueprint(inmates.bp)
    app.register_blueprint(attendances.bp)
    app.register_blueprint(reports.bp)

    app.add_url_rule("/", endpoint="index")

    return app
