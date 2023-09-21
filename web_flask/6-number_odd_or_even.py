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


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ display Number n in header tag """
    return render_template("5-number_odd.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """ display Number: n is even|odd in sided a h1 tag """
    even_or_odd = ''
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, even_or_odd=even)
    else:
        return render_template("6-number_odd_or_even.html", n=n, even_or_odd=odd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
