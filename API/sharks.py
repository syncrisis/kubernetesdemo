from datetime import datetime

import flask
import pymysql
import json


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# Create a handler for our read (GET) Sharks
def read():
    """
    This function responds to a request for /api/sharks
    with the complete lists of sharks

    :return:        sorted list of sharks
    """
    data = get_data()

    return flask.Response(
        json.dumps(data),
        headers={'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST'},
        mimetype=u'application/json')
    # return [SHARKS[key] for key in sorted(SHARKS.keys())]


def get_data():
    connection = pymysql.connect(host='mysql-db',
                                 user='root',
                                 password='sharksAreCool!!',
                                 db='sharks',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:

            cursor.execute(
                """SELECT Shark.*, Species.Name As SpeciesName,Species.FriendlyName, Lat, Lng
                FROM Shark 
                join Species on Shark.SpeciesId = Species.Id 
                join Ping on Shark.LastPingId = Ping.Id""")

            results = cursor.fetchall()

            sharks = []
            for shark in results:
                entry = {
                    'Id': shark['Id'],
                    'Name': shark['Name'],
                    'Lat': shark['Lat'],
                    'Lng': shark['Lng'],
                    'Species': shark['SpeciesName'],
                    'SpeciesId': shark['SpeciesId'],
                    'TagDate': str(shark['TagDate']),
                    'LatestPing': str(shark['LatestPing']),
                    'Age': shark['Age'],
                    'Length': str(shark['Length']),
                    'FriendlyName': shark['FriendlyName'],
                    'Image': shark['ImageLink'],
                }
                sharks.append(entry)

        return sharks
    finally:
        connection.close()
