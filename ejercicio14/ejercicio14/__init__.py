from flask import Flask, jsonify
from config import Config

def init_app():
    """Crea y configura la aplicacion Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
@app.route(/balance/<string:input>, methods=['GET'])
def balace_sym(input):
    stack = ArrayStack()
    open_symbols = "([{"
    close_symbols = ")]}"
    map = {')': '(', ']', '[', '}', '{'}

    for symbol in input:
        if symbol in open_symbols:
            stack.push(symbol)
        elif symbol in close_symbols:
            if stack.is_empty() or stack.top() != map[symbol]:
                return {'balanced': False}
            stack.pop()
    return {'balanced':stack.is_empty()}