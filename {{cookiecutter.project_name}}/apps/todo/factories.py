from datetime import timedelta

import factory
from django.utils import timezone
from factory import RelatedFactoryList
from factory.django import DjangoModelFactory

from .models import TodoList, TodoItem


class TodoListFactory(DjangoModelFactory):
    class Meta:
        model = TodoList

    title = factory.Faker('sentence', nb_words=3, variable_nb_words=True)

    # Creating a related factory list for TodoItem instances
    items = RelatedFactoryList(
        'apps.todo.factories.TodoItemFactory',
        factory_related_name='todo_list',
        size=5
    )


class TodoItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TodoItem

    title = factory.Faker('sentence', nb_words=5, variable_nb_words=True)
    description = factory.Faker('paragraph', nb_sentences=3, variable_nb_sentences=True)
    due_date = timezone.now() + timedelta(days=7)
    todo_list = factory.SubFactory(TodoListFactory)
