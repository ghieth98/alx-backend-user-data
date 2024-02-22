#!/usr/bin/env python3
"""
User authentication
"""

from bcrypt import hashpw, gensalt

from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """
    Hash password with bcrypt
    """
    return hashpw(password.encode('utf8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user
        """
        user_email = self._db.find_user_by(email=email)
        if not user_email:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError(f"User <user's email> already exists")
