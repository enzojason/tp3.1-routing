#ejercicio 6
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