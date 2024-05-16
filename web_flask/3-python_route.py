#!/usr/bin/python3
"""Write a script that starts a Flask web application"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route("/")
def hello():
    return 'Hello HBNB!'


@app.route("/hbnb")
def hbnb_hbnb():
    return 'HBNB'


@app.route("/c/<text>")
def hbnb_hbnb_c(text):
    word  = 'C {}'.format(escape(text)).replace('_',' ')
    return word

@app.route("/python/<text>", strict_slashes = False)
def hbnb_hbnb_python(text='is cool'):
    word  = 'Python {}'.format(escape(text)).replace('_',' ')
    return word

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
