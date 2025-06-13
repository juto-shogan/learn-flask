from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    response = make_response('hello world')
    response.status_code = 202
    response.headers['Content-Type'] = 'application/octet-stream'
    return response
    
@app.route('/greet/<name>')
def greet(name):
    return f'hello {name}'

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f'The sum of {a} and {b} is {a + b}'

@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and name in request.args.keys():
        greeting = request.args['greeting']
        name = request.args.get('name')
        return f'{greeting}, {name}!'
    else:
        return 'Missing parameters! Please provide both greeting and name.'

if  __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')