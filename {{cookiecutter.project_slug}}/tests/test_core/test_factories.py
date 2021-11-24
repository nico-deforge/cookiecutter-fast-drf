import pytest

from {{cookiecutter.project_slug}}.core.models import User


@pytest.mark.django_db
def test_user_factory(user_factory):
    user = user_factory()
    assert User.objects.count() == 1
    assert user.check_password("Testable44")
