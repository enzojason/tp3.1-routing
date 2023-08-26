#ejercicio 10
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