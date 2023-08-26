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
        dob_date = datetime.datetime.strptime(dob,'%Y-%m-%d').date()
        current_date = datetime.datetime.now().date()
        if dob_date > current_date:
            return{'error': 'La fecha de nacimiento...es mayor a la actual'}
        else:
            return  {'edad':edad}

    #ejercicio 6
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
                return f'La división no está definida para el denominador 0'
        else:
            return f'Operación no válida: {operacion}'
        return {'resultado': resultado }

    #ejercicio 7
    @app.route('/operate', methods=['GET'])
    def operacion_num():
        operacion = request.args.get('operacion')
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        
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
        elif 'error' in age.keys():
            return age
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
    

    #ejercicio 13
    @app.route('/convert/binary/<string:num>')
    def convierteBinario_Decimal(num):
        if not all(c in '01' for c in num):
            return "El numero ingresado no es binario"
        
        decimal_num = 0
        for i, dig in enumerate(reversed(num)):
            decimal_num += int(dig) * (2 ** i)
    
        return str(decimal_num)


    #ejercicio 14
    @app.route('/balance/<string:input>')
    def verificar(input):
        class Stack:
            def __init__(self):
                self._data = []
            
            def push(self, item):
                self._data.append(item)

            def pop(self):
                if not self.is_empty():
                    return self._data.pop()
                else:
                    return {"error": "La pila esta vacia"}

            def top(self):
                if not self.is_empty():
                    return self._data[-1]
                else:
                    return {"error": "La pila esta vacia"}
            
            def is_empty(self):
                return len(self._data) == 0
            
            def __len__(self):
                return len(self._data)
            
        def balanceador(expresion):
            stack = Stack()
            limiters = {')':'(', '}':'{', ']':'['}
            for character in expresion:
                if character in '([{':
                    stack.push(character)
                elif character in ')]}':
                    if stack.is_empty() or stack.top() != limiters[character]:
                        return False
                    stack.pop()
            return stack.is_empty()

        expresion = input
        if balanceador(expresion):
            return {"balanced": True}
        else:
            return {"balanced": False}
        

    return app
