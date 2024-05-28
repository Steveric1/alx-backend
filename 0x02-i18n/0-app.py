#!/usr/bin/env python3

"""
Setting up a bask flask app to create a single / route 
and an index.html template that simply outputs 'Welcome to Holberton'
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

# Create a sigle route


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
