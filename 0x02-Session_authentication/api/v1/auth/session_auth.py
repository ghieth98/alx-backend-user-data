#!/usr/bin/env python3
""" Module of Session Auth
"""
import uuid
from typing import Dict

from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    """ Session Auth"""
    user_id_by_session_id: Dict[str, str] = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a new session id for user
        """

        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Get user id for the session
        """

        if session_id is None or type(session_id) is not str:
            return None

        return self.user_id_by_session_id[session_id]

    def current_user(self, request=None):
        """ Current User
        """
        session_cookie = self.session_cookie(request)

        if session_cookie is None:
            return None

        user_id = self.user_id_for_session_id(session_cookie)

        return User.get(user_id)
