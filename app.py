from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/about')
def message():
    return 'This here is not a web page'

app.run(debug=True)