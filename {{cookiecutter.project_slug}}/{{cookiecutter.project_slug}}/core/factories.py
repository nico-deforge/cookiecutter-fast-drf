import factory

from {{cookiecutter.project_slug}}.core.models import User


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: f"nicolas{n}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "Testable44")

    class Meta:
        model = User
