#ejercicio 12
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