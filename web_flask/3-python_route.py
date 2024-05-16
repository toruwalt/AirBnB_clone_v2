#!/usr/bin/python3
"""Write a script that starts a Flask web application

        The application listens on 0.0.0.0, port 5000.
    Routes:
        /: Displays 'Hello HBNB!'.
        /hbnb: Displays 'HBNB'.
        /c/<text>: Displays 'C' followed by the value of <text>.
        /python/(<text>): Display 'Python' followed by the value of <text>

"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb_hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def hbnb_hbnb_c(text):
    return 'C {}'.format(escape(text)).replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hbnb_hbnb_python(text='is cool'):
    return 'Python {}'.format(escape(text)).replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
