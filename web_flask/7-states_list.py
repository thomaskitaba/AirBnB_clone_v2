#!/usr/bin/python3
""" 8- list states """
from flask import Flask, render_template
from models import *
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ H1 = States, ul states State: <state.id>: <B><state.name></B>
        list(storage.all('States')) output: [<State object>, <State object>
        ...
        ]
    """
    all_states = storage.all('State').value
    return render_template("7-states_list.html", all_states=all_states)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
