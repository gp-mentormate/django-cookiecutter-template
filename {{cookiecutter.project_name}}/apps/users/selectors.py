from django.contrib.auth.models import User


def all_users():
    return User.objects.all()
