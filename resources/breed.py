from flask_restful import Resource
import sqlite3


class Breeds(Resource):
    def get(self):
        connector = sqlite3.connect('site.db')
        cursor = connector.cursor()
        result = cursor.execute('SELECT name FROM breeds')
        return [row[0] for row in result.fetchall()], 200


class Breed(Resource):
    def get(self, name):
        connector = sqlite3.connect('site.db')
        cursor = connector.cursor()
        query = 'SELECT * FROM breeds where name=?'
        result = cursor.execute(query, (name,))
        info = result.fetchone()
        keys = ('id', 'name', 'size', 'height',
                'weight', 'coat', 'energy', 'activities')
        return dict(zip(keys, info))
