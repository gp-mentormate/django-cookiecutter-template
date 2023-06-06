from django.contrib.auth.models import AbstractUser

from apps.core.models import BaseModel


class CustomUser(AbstractUser, BaseModel):
    """
    CustomUser class represents a custom user model
    that extends the AbstractUser and BaseModel classes.

    This class provides additional functionality and
    customization options for user management within the 'users' app.
    """

    class Meta:
        app_label = 'users'
