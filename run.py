from flask import Flask
from flask_restful import Api, Resource
from resources.breed import Breeds, Breed

app = Flask(__name__)

api = Api(app)

api.add_resource(Breeds, '/breeds')
api.add_resource(Breed, '/breeds/<name>')


if __name__ == "__main__":
    app.run(debug=True)
