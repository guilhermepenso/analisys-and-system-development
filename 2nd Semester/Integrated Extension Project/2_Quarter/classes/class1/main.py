from flask import Flask

app = Flask(__name__)
    
#Creating a route (each route is a call for a web page)

@app.route('/')
def hello():
    return 'Hello World!!!'

@app.route('/test') #localhost:5000/test
def test():
    return "You're running the test route!!!"

@app.route('/list') #localhost:5000/list
def list():
    names = ['Mary', 'Anna','Cezar', 'Bolsonaro', 'Jonathan'  ]
    return names

@app.route('/enter/<value>') #localhost:5000/enter/
def enter(value):
    return f"You've typed this: {value}"

@app.route('/squared/<number>') #localhost:5000/squared/
def squared(number):
    num = float(number)
    return f"Result: {num ** 2}"

@app.route('/add/<n1>/<n2>') #localhost:5000/add/
def add(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    return f'Result: {n1 + n2}'


@app.route('/subb/<n1>/<n2>') #localhost:5000/add/
def subb(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    return f'Result: {n1 - n2}'


@app.route('/mult/<n1>/<n2>') #localhost:5000/add/
def mult(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    return f'Result: {n1 * n2}'


@app.route('/div/<n1>/<n2>') #localhost:5000/add/
def div(n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    return f'Result: {n1 / n2}'

@app.route('/calc/<n1>/<op>/<n2>')
def calc(n1, op, n2):
    n1 = float(n1)
    n2 = float(n2)
    if op == "+":
        return f'Result: {n1 + n2}'
    elif op == "-":
        return f'Result: {n1 - n2}'
    elif op == "*":
        return f'Result: {n1 * n2}'
    elif op == ":":
        if n2 == 0:
            return f"Can't divide by zero"
        else:
            return f'Result: {n1 / n2}'
    else:
        return f'Operation not supported'

if __name__ == '__main__':
    app.run(debug=True)