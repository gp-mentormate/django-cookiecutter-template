# The `serializers.py` file is responsible for defining serialization
# and deserialization logic to convert complex data types, such as
# model instances, into JSON or other formats for API responses and vice versa.
# Create your services here.

from typing import Union

from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.db.models import QuerySet

from apps.todo.api.v1.selectors import all_todo_lists, user_todo_lists


def get_todo_lists(*, user: Union[AbstractUser, AnonymousUser]) -> QuerySet:
    if user.is_superuser:
        return all_todo_lists()
    elif user.is_authenticated:
        return user_todo_lists(user=user)
    else:
        return QuerySet.none()
