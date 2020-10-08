from flask import Blueprint, jsonify
from .. import connection

api = Blueprint('api', __name__, url_prefix='/api')

def fetch_records(query, field):
    """
    args: query(SQL statement as a string ), field(filter for SQL statement)
    returns: JSON object
    This function returns a JSON object of all records matching the
    SQL query statement
    """
    records = None
    field = field.upper()
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(query, (field,))
            records = cursor.fetchall()

    # perform conversion to geoJSON for display on mapbox
    features = [{"type": "Feature",
                    "geometry" : {
                        "type": "Point",
                        "coordinates": [rec[0], rec[1]],
                    },
                    "properties" : rec} for rec in list(records)]
    return jsonify(features)


@api.route('/boroughs/<string:borough>', methods=['GET'])
def boroughs(borough):
    select_query = "select longitude, latitude from collisions where borough = %s"
    return fetch_records(select_query, borough)


@api.route('/zipcodes/<string:zipcode>', methods=['GET'])
def zipcodes(zipcode):
    select_query = "select longitude, latitude from collisions where zipcode = %s"
    return fetch_records(select_query, zipcode)
