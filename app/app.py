from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello %s"%name

if __name__ == '__main__':
    app.run(port=8000)
