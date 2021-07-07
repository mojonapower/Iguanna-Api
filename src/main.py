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
from models import db, Teacher, Materia, Student
import secrets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
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

@app.route('/teacher', methods=['GET'])
def handle_hello():
    
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200
############### ver materias #####################
@app.route('/materia', methods=['GET'])
def get_materia():

    all_materia = Materia.query.all()
    all_materia = list(map(lambda x: x.serialize(), all_materia))
    
    response_body = {
        "result": all_materia
    }
    return jsonify(response_body), 200
############### END ver materias #####################

############### ver ESTUDIANTES #####################
@app.route('/estudiantes', methods=['GET'])
def get_estudiantes():
    all_students = Student.query.all()
    all_students = list(map(lambda x: x.serialize(), all_students))
    
    response_body = {
        "msg": all_students
    }

    return jsonify(response_body), 200
############### END ver ESTUDIANTES #####################

############### crear ESTUDIANTES #####################
@app.route('/estudiantes', methods=['POST'])
def post_estudiantes():
    
    body = request.get_json()
    password = secrets.token_hex(5)
    
    if body is None:
            return "The request body is null", 400
    if 'curso' not in body:
        return 'Especificar curso',400
    if 'nombre' not in body:
        return 'Especificar nombre', 400

    new = Student(nombre=body['nombre'], curso= body['curso'], password=password)
    db.session.add(new)
    db.session.commit()
    response_body = {
        "msg": "Estudiante Registrado"
    }

    return jsonify(response_body), 200
############### END crear ESTUDIANTES #####################

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
