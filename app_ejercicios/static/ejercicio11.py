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

