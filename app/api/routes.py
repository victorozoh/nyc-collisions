from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/boroughs/<string:borough>')
def boroughs(borough):
    return {'one' : borough}