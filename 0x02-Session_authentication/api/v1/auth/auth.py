#!/usr/bin/env python3
"""
Module of auth views
"""
from typing import List, TypeVar

from flask import request


class Auth:
    """ Auth Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Checks if the auth is required"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'

        for i in excluded_paths:
            if i == path or path.startswith(i.split('*')[0]):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Returns the authorization header"""
        if not request:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Returns the current user"""

        return None
