#ejercicio 5
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