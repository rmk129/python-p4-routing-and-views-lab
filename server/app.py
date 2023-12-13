#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def param(parameter):
    print(f'{parameter}')
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    number = ""
    for x in range(parameter):
        number += f'{x}' + "\n"
    return number
    
# @app.route('/math/<int:num1><operation><int:num2>')
# def math(num1, operation, num2):
#     print(isinstance(num1, int))

    
