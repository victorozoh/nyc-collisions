from flask import Flask

from .api.routes import api
from .home.routes import homepage

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(homepage)

    return app
