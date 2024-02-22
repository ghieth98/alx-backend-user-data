#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, jsonify

from auth import Auth

app = Flask(__name__)
app.url_map.strict_slashes = False

AUTH = Auth()

app.route('/')


def hello():
    """return Bienvenue"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
