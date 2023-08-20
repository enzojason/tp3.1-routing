from flask import Flask,request
from config import Config

def init_app():
    app=Flask(__name__,static_folder=Config.STATIC_FOLDER,template_folder=Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    
    #ejercicio 1
    @app.route('/')
    def hello_world():
        return 'Bienvenidx'

    #ejercicio 2
    @app.route('/info')
    def bienvenida_info():
        return 'Bienvenidx a '+ app.config['APP_NAME']

    #ejercicio 3
    @app.route('/about')
    def about_funcion():
        return {
            'app_name':app.config['APP_NAME'],
            'description':app.config['DESCRIPTION'],
            'version':app.config['VERSION'],
            'developers':app.config['DEVELOPERS']
        }
    

    #ejercicio 4
    @app.route('/sum/<int:num1>/<int:num2>')
    def sumar(num1,num2):
        resultado=num1+num2
        return  {'resultado':resultado}

    #ejercicio 5
    @app.route('/age/<dob>')
    def calcular_edad(dob):
        import datetime
        fecha_nacimiento = datetime.datetime.strptime(dob, '%Y-%m-%d')
        edad = datetime.datetime.now().year - fecha_nacimiento.year
        return  {'edad':edad}
    
    #ejercicio 6
    @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')
    def operar(operation,num1,num2):
        if operation=="sum":
            resultado=num1+num2
            return  {'resultado':resultado}
    
        if operation=="sub":
            resultado=num1*num2
            return  {'resultado':resultado}

        if operation=="mult":
            resultado=num1*num2
            return  {'resultado':resultado}

        if operation=="div":
            resultado=num1/num2
            return  {'resultado':resultado}

    #ejercicio 7
    @app.route('/operate')
    def opera():
        operation = request.args.get('operation')
        num1=request.args.get('num1')
        num2=request.args.get('num2')
        if operation=="sum":
            resultado=num1+num2
            return  {'Respuesta':resultado}
    
        if operation=="sub":
            resultado=num1*num2
            return  {'Respuesta':resultado}

        if operation=="mult":
            resultado=num1*num2
            return  {'Respuesta':resultado}

        if operation=="div":
            resultado=num1/num2
            return  {'Respuesta':resultado}
    
    #ejercicio 8
    @app.route('/title/<string:word>')
    def formatear(word):
        word=word.lower()
        word=word.capitalize()
        return { 'formatted_word': word}
    
    #ejercicio 9
    @app.route('/formatted/<string:dni>')
    def convertir_dni(dni):
        dni=dni.replace('-','')
        dni=dni.replace('.','')
        if len(str(dni))==8 and int(dni)>10000000:
            return {'formatted_dni': dni}
        else:
            return {'error': 'dni invalido'}

    #ejercicio 10
    @app.route('/format')
    def consultar():
        firstname=formatear(request.args.get('firstname'))
        lastname=formatear(request.args.get('lastname'))
        age=calcular_edad(request.args.get('dob'))
        dni=convertir_dni(request.args.get('dni'))

        if 'error' in dni.keys():
            return dni
        else:
            return {
                    'firstname': firstname["formatted_word"],
                    'lastname': lastname["formatted_word"],
                    'age': age["edad"],
                    'dni': dni["formatted_dni"]
                    }
    #ejercicio 11
    @app.route('/encode/<string:keyword>')
    def codificar(keyword):
        import json
        code=[]
        with open("./static/morse_code.json",'r') as archivo:
            data = json.load(archivo)
        for letra in keyword:
            datas=data['letters']
            if letra=="+":
                letra=" "
            for a,b in datas.items():
                if letra.upper() == a:
                    code.append(b)
                    code.append("+")
        code="".join(code)
        return code
                    
    #ejercicio 12
    @app.route('/decode/<string:morse_code>')
    def decodificar(morse_code):
        import json
        code=[]
        codigox=[]
        with open("./static/morse_code.json",'r') as archivo:
            data = json.load(archivo)
        datas=data['letters']
        for codigo in str(morse_code)+"+":
            if codigo=="+":
                codigox="".join(codigox)
                for a,b in datas.items():
                    if codigox == b:
                        code.append(a)
                codigox=[]
            else:
                codigox.append(codigo)
        code="".join(code)
        return code
                

    return app
