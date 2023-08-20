from flask import Flask, jsonify
from config import Config
from flask import render_template, request
import datetime
import re
import json
from urllib.parse import unquote

def init_app():
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, templates_folder = Config.TEMPLATES_FOLDER)
    app.config.from_object(Config)
# Endpoint que recibe los datos de un usuario como parámetros.
@app.route('/format', methods=['GET'])
def format_usuario():
    firstname = request.args.get('firstname').capitalize()
    lastname = request.args.get('lastname').capitalize()
    dob = request.args.get('dob')
    dni = request.args.get('dni')

    dob_date = datetime.datetime.strptime(dob,'%Y-%m-%d').date()
    current_date = datetime.datetime.now().date()

    if dob_date > current_date:
        return jsonify({'error': 'La fecha de nacimiento...'})
    
    dni_clean = re.sub(r'[.-]', '', dni)
    if dni_clean.isdigit() and len(dni_clean) == 8:
        dni_formated = int(dni_clean)
        age = (current_date - dob_date).days // 365
        user_info = {
            'firstname': firstname,
            'lastname': lastname,
            'age': age,
            'dni': dni_formated,
        }
        return jsonify(user_info)
    else:
        return jsonify({'error': 'DNI no válido'})