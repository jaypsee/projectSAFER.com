from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def index(name):
    return '<h1><a href="/alerts.html">Hello</a> {}!</h1>'.format(name)