"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Starships, Vehicles, Favorite
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#endpoints
#obtener todos los user
@app.route('/user', methods=['GET'])
def handle_hello():

    user_querys = User.query.all()
    results = list(map(lambda item: item.serialize(),user_querys))

    if results == []:
        return jsonify({"msg":"No hay user"}), 404
    
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "results": results
    }

    return jsonify(response_body), 200

#obtener un user
@app.route('/user/<int:user_id>', methods=['GET'])
def get_one_user(user_id):

    user_query = User.query.filter_by(id=user_id).first()

    if  user_query is None:
         return jsonify({"msg":"El user no existe"}), 404

    response_body = {
         "msg": "Hello, estos son tus user",
         "result": user_query.serialize()
     }

    return jsonify(response_body), 200

#obtener todos los People
@app.route('/people', methods=['GET'])
def get_people():

    people_querys = People.query.all()

    results = list(map(lambda item: item.serialize(),people_querys))

    if results == []:
        return jsonify({"msg":"No hay people"}), 404

    response_body = {
        "msg": "Hello, estos son tus people",
        "results": results
     }
    
    return jsonify(response_body), 200

#obtener un People
@app.route('/people/<int:people_id>', methods=['GET'])
def get_one_people(people_id):

    people_query = People.query.filter_by(id=people_id).first()

    if  people_query is None:
         return jsonify({"msg":"El people no existe"}), 404

    response_body = {
         "msg": "Hello, estos son tus people",
         "result": people_query.serialize()
     }

    return jsonify(response_body), 200

#obtener todos los Planets
@app.route('/planets', methods=['GET'])
def get_planets():

    planets_querys = Planets.query.all()

    results = list(map(lambda item: item.serialize(),planets_querys))

    if results == []:
        return jsonify({"msg":"No hay planetas"}), 404

    response_body = {
        "msg": "Hello, estos son tus planetas",
        "results": results
     }
    
    return jsonify(response_body), 200

#obtener un Planets
@app.route('/planets/<int:planets_id>', methods=['GET'])
def get_one_planets(planets_id):

    planets_query = Planets.query.filter_by(id=planets_id).first()

    if  planets_query is None:
         return jsonify({"msg":"El planets no existe"}), 404

    response_body = {
         "msg": "Hello, estos son tus planets",
         "result": planets_query.serialize()
     }

    return jsonify(response_body), 200

#obtener todos los Starships
@app.route('/starships', methods=['GET'])
def get_starships():

    starships_querys = Starships.query.all()

    results = list(map(lambda item: item.serialize(),starships_querys))

    if results == []:
        return jsonify({"msg":"No hay starship"}), 404

    response_body = {
        "msg": "Hello, estos son tus starships",
        "results": results
     }
    
    return jsonify(response_body), 200

#obtener solo un Starships
@app.route('/starships/<int:starships_id>', methods=['GET'])
def get_one_starships(starships_id):

    starships_query = Starships.query.filter_by(id=starships_id).first()

    if  starships_query is None:
         return jsonify({"msg":"El starship no existe"}), 404

    response_body = {
         "msg": "Hello, estos son tus starships",
         "result": starships_query.serialize()
     }

    return jsonify(response_body), 200

#obtener todos los Vehicles
@app.route('/vehicles', methods=['GET'])
def get_vehicles():

    vehicles_querys = Vehicles.query.all()

    results = list(map(lambda item: item.serialize(),vehicles_querys))

    if results == []:
        return jsonify({"msg":"No hay vehicles"}), 404

    response_body = {
        "msg": "Hello, estos son tus vehicles",
        "results": results
     }
    
    return jsonify(response_body), 200

#obtener un Vehicles
@app.route('/vehicles/<int:vehicles_id>', methods=['GET'])
def get_one_vehicles(vehicles_id):

    vehicles_query = Vehicles.query.filter_by(id=vehicles_id).first()

    if  vehicles_query is None:
         return jsonify({"msg":"El vehicle no existe"}), 404

    response_body = {
         "msg": "Hello, estos son tus vehicles",
         "result": vehicles_query.serialize()
     }

    return jsonify(response_body), 200

#obtener todos los favorite
@app.route('/favorite', methods=['GET'])
def get_favorite():

    favorite_querys = Favorite.query.all()

    results = list(map(lambda item: item.serialize(),favorite_querys))

    if results == []:
        return jsonify({"msg":"No hay favorites"}), 404

    response_body = {
        "msg": "Hello, estos son tus favorites",
        "results": results
     }
    
    return jsonify(response_body), 200

#obtener un favorite
@app.route('/favorite/<int:favorite_id>', methods=['GET'])
def get_one_favorite(favorite_id):

    favorite_query = Favorite.query.filter_by(id=favorite_id).first()

    if  favorite_query is None:
         return jsonify({"msg":"El favorite no existe"}), 404

    response_body = {
         "msg": "Hello, estos son tus favorites",
         "result": favorite_query.serialize()
     }

    return jsonify(response_body), 200

#obtener de un planet
@app.route('/planets', methods=['POST'])
def create_planets():
    request_body = request.json
    print(request_body)

    planets_query = Planets.query.filter_by(name=request_body["name"]).first()
    print(planets_query)

    if  planets_query is None:
          new_planets = Planets(name=request_body["name"], population=request_body["population"])
          db.session.add(new_planets)
          db.session.commit()
        #   return jsonify({"msg":"El planeta no existe"}), 404

          response_body = {
             "msg": "Planeta creado",
        #  "result": planets_query.serialize()
          }

          return jsonify(response_body), 200
    else:
          return jsonify({"msg":"planeta ya existente"}), 400
    
#obtener de favorito
@app.route('/favorites', methods=['POST'])
def create_favorite():
    request_body = request.json

    favorite = Favorite.query.filter_by(user=request_body["user_id"], planet_id=request_body["planet_id"]).first()

    if favorite is None:
        new_favorite = Favorite(user=request_body["user_id"], planet_id=request_body["planet_id"])
        db.session.add(new_favorite)
        db.session.commit()

        response_body = {
            "msg": "Favorito creado"
        }

        return jsonify(response_body), 200
    else:
        return jsonify({"msg": "El favorito ya existe"}), 400   

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
