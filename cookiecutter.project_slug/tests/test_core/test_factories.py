import pytest

from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_user_factory(user_factory):
    user = user_factory()
    assert User.objects.count() == 1
    assert user.check_password("Testable44")
