#!/usr/bin/env python3
"""
User authentication
"""

from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """
    Hash password with bcrypt
    """

    return hashpw(password.encode('utf8'), gensalt())
