#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """  return Hello HBNB! """
    return " “Hello HBNB!”"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ return HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C(text):
    """ return C and text provided"""
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ diplay Python and text value """
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ display n is a number if only n is integer """
    try:
        if isinstance(n, int):
            return f"{n} is a number"
    except TypeError:
        return None


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
