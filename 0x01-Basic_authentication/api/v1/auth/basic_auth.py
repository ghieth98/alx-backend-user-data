#!/usr/bin/enn python3
"""Basic auth class"""
import base64
from typing import TypeVar

from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """Basic auth class"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract basic authorization based on base64"""
        if authorization_header is None or type(
                authorization_header) is not str or not authorization_header.startswith(
            'Basic '):
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) -> str:
        """Decode basic authorization"""
        if base64_authorization_header is None or type(
                base64_authorization_header) is not str:
            return None

        try:
            return base64.b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self, decoded_authorization_header: str) -> (
            str, str):
        """Extract user"""
        if decoded_authorization_header is None or type(
                decoded_authorization_header) is not str or ':' not in decoded_authorization_header:
            return None, None

        return decoded_authorization_header.split(':', 1)

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Return user instance based on user_email and user_pwd"""

        if user_email is None or type(user_email) is not str:
            return None

        if user_pwd is None or type(user_pwd) is not str:
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return current user instance"""

        header = self.authorization_header(request)
        to_base64 = self.extract_base64_authorization_header(header)
        decode = self.decode_authorization_header(to_base64)
        extract = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(*extract)