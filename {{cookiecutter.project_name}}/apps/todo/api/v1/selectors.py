# The `selectors.py` module contains the implementation of selectors,
# which are specialized components within an application that handle
# the logic of pulling information from the database. They act as a
# "sub-layer" to services, focusing on the retrieval of data rather
# than modifying it. Selectors encapsulate the queries and filtering
# operations necessary to retrieve specific data sets, making
# the database interaction more efficient and reusable across different
# parts of the application.

from django.db.models import QuerySet

from apps.todo.models import TodoList
from apps.users.models import CustomUser


def all_todo_lists() -> QuerySet:
    return TodoList.objects.all()


def user_todo_lists(*, user: CustomUser) -> QuerySet:
    return TodoList.objects.filter(created_by=user)
