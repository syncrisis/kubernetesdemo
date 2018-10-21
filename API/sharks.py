from datetime import datetime

import flask
from flask import make_response, abort
import pymysql
import json


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Data to serve with our API
SHARKS = {
    "Farrell": {
        "fname": "Doug",
        "lname": "Farrell",
        "timestamp": get_timestamp()
    },
    "Brockman": {
        "fname": "Kent",
        "lname": "Brockman",
        "timestamp": get_timestamp()
    },
    "Easter": {
        "fname": "Bunny",
        "lname": "Easter",
        "timestamp": get_timestamp()
    }
}


# Create a handler for our read (GET) Sharks
def read():
    """
    This function responds to a request for /api/sharks
    with the complete lists of sharks

    :return:        sorted list of sharks
    """
    data = getData()
    return flask.Response(json.dumps({
        'Id': data['Id'],
        'Name': data['Name'],
        'Lat': data['Lat'],
        'Lng': data['Lng'],
        'Species': data['SpeciesName'],
        'SpeciesId': data['SpeciesId'],
        'TagDate': str(data['TagDate']),
        'LatestPing': str(data['LatestPing']),
        'Age': data['Age'],
        'Length': str(data['Length']),
        'FriendlyName': data['FriendlyName'],
        'Image': data['ImageLink'],
    }), headers={'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST'},
        mimetype=u'application/json')
    # return [SHARKS[key] for key in sorted(SHARKS.keys())]


def create(shark):
    """
    This function creates a new shark in the shark structure
    based on the passed in shark data
    :param shark:  shark to create in people structure
    :return:        201 on success, 406 on shark exists
    """
    lname = shark.get("lname", None)
    fname = shark.get("fname", None)

    # Does the person exist already?
    if lname not in SHARKS and lname is not None:
        SHARKS[lname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        return make_response(
            "{lname} successfully created".format(lname=lname), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Peron with last name {lname} already exists".format(lname=lname),
        )


def getData():
    connection = pymysql.connect(host='mysql-db',
                                 user='root',
                                 password='sharksAreCool!!',
                                 db='sharks',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:

            cursor.execute(
                'SELECT Shark.*, Species.Name As SpeciesName,Species.FriendlyName, Lat, Lng FROM Shark join Species on Shark.SpeciesId = Species.Id join Ping on Shark.LastPingId = Ping.Id')
            results = cursor.fetchone()

        return results
    finally:
        connection.close()
