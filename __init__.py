import re
from flask import Flask
from config import Config
def init_app():
    """Crea y configura la aplicación Flask"""
    """Ejercicios del TP 4, 7 (hace NOe),8 y 13"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    # Un endpoint que dice 'Hola Mundo!'
    @app.route('/')
    def hello_world():
        return 'Hola Mundo!'
    @app.route('/academia')
    @app.route('/home')
    def bienvenida():
        return 'Bienvenidx a la Academia!'
    @app.route('/help/')
    def help():
        return 'Soporte de la aplicación'
    @app.route('/about')
    def about():
        return 'Información acerca de la aplicación'
    @app.route('/perfil/<username>')
    def perfil(username):
        """Mensaje de bienvenida a un usuario"""
        return f'Bienvenido {username}!'
    
    """Ejercicio 4"""
    @app.route('/sum/<int:num1>/<int:num2>')
    def sum(num1, num2):
        resultados = num1 + num2
        return f'La suma de {num1} y {num2} es {resultados}.'
    
    """Ejercicio 8"""
    @app.route('/title/<string:word>')
    def formatoTitulo(word):
        titulo= word.capitalize()
        formatted_word = {'formatted_word': titulo}
        return formatted_word

    """Ejercicio 9"""
    @app.route('/formatted/<string:dni>')
    def formatoDNI(dni):
        #def to_python(self, value):
        # Eliminar caracteres no numéricos (puntos, guiones, etc.)
        dni_digits = re.sub(r'\D', '', dni)
        # Validar que tenga 8 dígitos numéricos
        if len(dni_digits) != 8:
            return (f'error: DNI no válido'), 400
        
        formatted_dni = {'formatted_dni': dni_digits}
        return formatted_dni


    """Ejercicio 13"""
    @app.route('/convert/binary/<string:num>')
    def convierteBinario_Decimal(num):
        if not all(c in '01' for c in num):
            return "El numero ingresado no es binario"
        
        decimal_num = 0
        for i, dig in enumerate(reversed(num)):
            decimal_num += int(dig) * (2 ** i)
    
        return str(decimal_num)

    return app