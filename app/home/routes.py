from flask import Blueprint, render_template

homepage = Blueprint('index', __name__)

@homepage.route('/')
def home():
    return render_template('index.html')
