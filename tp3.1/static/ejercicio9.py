#ejercicio 9
def convertir_dni(dni):
    dni=dni.replace('-','')
    dni=dni.replace('.','')
    if len(str(dni))==8 and int(dni)>10000000:
        return {'formatted_dni': dni}
    else:
        return {'error': 'dni invalido'}