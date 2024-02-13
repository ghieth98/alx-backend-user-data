#!/usr/bin/enn python3
"""Basic auth class"""
import base64

from api.v1.auth import auth


class BasicAuth(auth):
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
