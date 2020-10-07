from flask import Flask
from config import Config
import psycopg2


application = Flask(__name__)
# configure the Flask app
application.config.from_object(Config)
DB_URI = application.config['POSTGRESQL_URI']

# Get Heroku database connection
connection = psycopg2.connect(DB_URI)

# register routes
from .api.routes import api
from .home.routes import homepage
application.register_blueprint(api)
application.register_blueprint(homepage)
