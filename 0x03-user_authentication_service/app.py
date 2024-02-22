#!/usr/bin/env python3
"""Basic flask app"""

from flask import Flask, jsonify, request

from auth import Auth

app = Flask(__name__)
app.url_map.strict_slashes = False

AUTH = Auth()

app.route('/')


def hello():
    """return Bienvenue"""
    return jsonify({"message": "Bienvenue"})


app.route('/users', methods=['POST'])
def users():
    """base users path"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    return jsonify({"email": email, "message": "user created"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
