from flask import Flask
from config import Config

def init_app():
    app=Flask(__name__,static_folder=Config.STATIC_FOLDER,template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    
    @app.route('/')
    def hello_world():
        return 'hola mundo'

    @app.route('/info')
    #un end point
    def bienvenida_info():
        return 'Bienvenidx a Routing App'

    return app
