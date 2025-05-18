from flask import Flask, request

app = Flask(__name__)

@app.route('/calculate')
def calculate():
    a = request.args.get('a')
    b = request.args.get('b')
    operator = \
    request.args.get('operator')
    if a and b and operator:
        a = int(a)
        b = int(b)
        if operator == 'add':
            result = a + b
        elif operator == 'substract':
            result = a - b
        elif operator == 'multiply':
            result = a * b
        elif operator == 'divide':
            result = a / b
        return f'{ a } { operator } { b } \
            = { result }'
    else:
        return 'Error: Insufficient \
            arguments'
    
app.run()

"""To use app, after running it i adress 
field sign GET request for /calculate"""