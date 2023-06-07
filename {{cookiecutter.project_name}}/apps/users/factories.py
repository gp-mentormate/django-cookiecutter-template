import factory
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password123")

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """
        Override the default _create method to disable password hashing
        during tests.
        """
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)
