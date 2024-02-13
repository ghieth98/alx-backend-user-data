#!/usr/bin/enn python3
"""Basic auth class"""
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
