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

if __name__ == '__main__':
    app.run(debug=True)