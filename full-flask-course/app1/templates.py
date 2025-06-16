from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    myvalue = 'Hello, Flask!'
    result = myvalue + ' - This is a Flask app!'
    list = [1, 2, 3, 4, 5]
    return render_template('index.html', myvalue=myvalue, result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 