import factory

from .models import User


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Sequence(lambda n: f"nicolas{n}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "Testable35")

    class Meta:
        model = User
