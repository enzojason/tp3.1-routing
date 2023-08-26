#ejercicio 13
def convierteBinario_Decimal(num):
    if not all(c in '01' for c in num):
        return "El numero ingresado no es binario"
    
    decimal_num = 0
    for i, dig in enumerate(reversed(num)):
        decimal_num += int(dig) * (2 ** i)

    return str(decimal_num)