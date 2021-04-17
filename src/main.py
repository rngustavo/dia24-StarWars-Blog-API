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
from models import db, User, People, Planets, Favorites
from data import listplanets, listpeople
#import JWT for tokenization
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# config for jwt
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
jwt = JWTManager(app)


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }
    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def people():    
    all_people = People.query.all()   
    all_people = list(map(lambda x: x.serialize(), all_people))

    #print(all_people) 
    #return thepeople.json, 200 -->ASI NO SIRVE
    #return jsonify(response_body), 200 -->ASI NO SIRVE
    return jsonify({"results":all_people, "message":"People's List"}), 200

@app.route('/planets', methods=['GET'])
def planets():    
    all_planets = Planets.query.all()   
    all_planets = list(map(lambda x: x.serialize(), all_planets))    
    return jsonify({"results":all_planets, "message":"Planets's List"}), 200

@app.route('/load', methods=['GET'])
def load_data():
    for planet in listplanets:
         new_planet=Planets()
         new_planet.name=planet["name"]
         new_planet.rotation_period =str(planet["rotation_period"])
         new_planet.orbital_period = planet["orbital_period"]
         new_planet.diameter = planet["diameter"]
         new_planet.climate = planet["climate"]
         new_planet.gravity = planet["gravity"]
         new_planet.terrain = planet["terrain"]
         new_planet.surface_water =  planet["surface_water"]
         new_planet.population =  planet["population"]
         new_planet.url = planet["url"]
         db.session.add(new_planet)
         db.session.commit()

    for person in listpeople:
        new_person=People()
        new_person.name=person["name"]  
        new_person.height = person["height"]
        new_person.hair_color =person["hair_color"]
        new_person.skin_color = person["skin_color"]
        new_person.eye_color = person["eye_color"]
        new_person.birth_year = person["birth_year"]
        new_person.gender = person["gender"]
        new_person.homeworld = person["homeworld"]
        new_person.url = person["url"]
        db.session.add(new_person)
        db.session.commit()

    response_body = {
        "msg": "loading... initial data to database...  "
    }
    return jsonify(response_body), 200




@app.route('/register', methods=['POST'])
def register_user():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    print('email', email)
    print('pass', password)
    # valida si estan vacios los ingresos
    if not email:
        return jsonify({"msg": "No email was provided"}), 400
    if not password:
        return jsonify({"msg": "No password was provided"}), 400
    
    # busca usuario en BBDD
    user = User.query.filter_by(email=email).first()
    if user:
        # the user was not found on the database
        return jsonify({"msg": "User already exists"}), 401
    else:
        # crea usuario nuevo
        new_user=User()
        new_user.email=email
        new_user.password=password  
        new_user.is_active=True     
        # crea registro nuevo en BBDD de 
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 200
    
@app.route('/login', methods=['POST']) 
def login():
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    # valida si estan vacios los ingresos
    if email is None:
        return jsonify({"msg": "No email was provided"}), 400
    if password is None:
        return jsonify({"msg": "No password was provided"}), 400

    # para proteger contraseñas usen hashed_password
    # busca usuario en BBDD
    user = User.query.filter_by(email=email, password=password).first()
    if user is None:
        return jsonify({"msg": "Invalid username or password"}), 401
    else:
        # crear token
        my_token = create_access_token(identity=user.id)
        return jsonify({"token": my_token})

@app.route("/protected", methods=['GET', 'POST'])
# protege ruta con esta funcion
@jwt_required()
def protected():
    # busca la identidad del token
    current_id = get_jwt_identity()
    # busca usuarios en base de datos
    user = User.query.get(current_id)
    print(user)
    return jsonify({"id": user.id, "email": user.email}), 200
    

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
