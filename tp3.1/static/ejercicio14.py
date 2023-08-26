#ejercicio 14
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