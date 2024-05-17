#!/usr/bin/python3
"""Write a script that starts a Flask web application

    The application listens on 0.0.0.0, port 5000.
    Routes:
        /: Displays 'Hello HBNB!'.
        /hbnb: Displays 'HBNB'.
        /c/<text>: Displays 'C' followed by the value of <text>.
        /python/(<text>): Display 'Python' followed by the value of <text>.
        /number/<n>: display “n is a number” only if n is an integer
        /number_template/<n>: display a HTML page only if n is an integer.
        /number_odd_or_even/<n>: display a HTML page only if n is an integer.
"""

from flask import Flask, render_template
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


@app.route("/number/<int:n>", strict_slashes=False)
def hbnb_hbnb_number(n):
    return '{} is a number'.format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def hbnb_hbnb_number_templates(n):
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def hbnb_hbnb_number_odd_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
