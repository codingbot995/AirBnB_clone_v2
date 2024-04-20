#!/usr/bin/python3
"""
A simple demostration of creating web app
"""
from flask import Flask

app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)

def index():
     return 'Hello HBNB!'

if __name__ == '__main__':
     app.run(host='127.0.0.1', port=5000)
