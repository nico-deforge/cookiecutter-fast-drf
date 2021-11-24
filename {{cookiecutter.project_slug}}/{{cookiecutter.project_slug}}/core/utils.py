from rest_framework.request import Request

from {{cookiecutter.project_slug}}.core.models import User


class AuthenticatedRequest(Request):
    user: User
