from flask import Flask
from ..config import Config
def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    # API que realiza operaciones matemáticas simples.
    @app.route('/operate/<string:operacion>/<int:num1>/<int:num2>')
    def operacion_num( operacion, num1, num2):
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