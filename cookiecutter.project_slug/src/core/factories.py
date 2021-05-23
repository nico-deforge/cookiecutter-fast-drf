import factory

from django.contrib.auth import get_user_model

User = get_user_model()


class UserFactory(factory.DjangoModelFactory):
    email = factory.Sequence(lambda n: f"nicolas{n}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "Testable44")

    class Meta:
        model = User
