from rest_framework.request import Request

from .models import User


class AuthenticatedRequest(Request):
    user: User
