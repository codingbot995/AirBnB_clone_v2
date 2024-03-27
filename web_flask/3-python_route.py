#!/usr/bin/python3
"""A simple demostration of creating web app"""
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
     return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
     return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def routing(text):
       return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def routing_2(text='is_cool'):
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)
