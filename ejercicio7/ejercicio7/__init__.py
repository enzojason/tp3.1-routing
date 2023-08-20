from flask import Flask
from config import Config
from flask import render_template, request
def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    # Ruta que recibe parámetros de consulta.
    @app.route('/operate', methods=['GET'])
    def operacion_num():
        operacion = request.args.get('operacion')
        num1 = init(request.args.get('num1'))
        num2 = init(request.args.get('num2'))
        
        if operacion == 'sum':
            resultado = num1 + num2
        elif operacion == 'sub' :
            resultado = num1 - num2
        elif operacion == 'mult' :
            resultado = num1 * num2
        elif operacion == 'div' :
            if num2 != 0:
                resultado = num1 / num2
            else:
                return {'La división no está definida para el denominador 0'}
        else:
            return f'Operación no válida: {operacion}'
        return {'resultado': resultado } 
    return app
