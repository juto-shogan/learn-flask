from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/hello')
def hello():
    return 'hello world'

@app.route('/greet/<name>')
def greet(name):
    return f'hello {name}'

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f'The sum of {a} and {b} is {a + b}'
``
if  __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')