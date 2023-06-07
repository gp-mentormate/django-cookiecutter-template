from datetime import timedelta

import factory
from django.utils import timezone
from factory import RelatedFactoryList
from factory.django import DjangoModelFactory

from .models import TodoItem, TodoList


class TodoListFactory(DjangoModelFactory):
    """
    TodoListFactory class represents a factory
    for creating TodoList instances.

    This factory class is used to generate fake
    TodoList objects for testing or seeding the database.

    Example usage:
        To create a TodoListFactory, call the factory and use the generated
        TodoList object:

        ```python
        todo_list = TodoListFactory()
        print(todo_list.title)
        print(todo_list.items.count())
        ```
    """

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
    """
    TodoItemFactory class represents a factory for creating
    TodoItem instances.

    This factory class is used to generate fake TodoItem
    objects for testing or seeding the database.

    Example usage:
        To create a TodoItemFactory, call the factory and use the generated
        TodoItem object:

        ```python
        todo_item = TodoItemFactory()
        print(todo_item.title)
        print(todo_item.description)
        print(todo_item.due_date)
        print(todo_item.todo_list.title)
        ```
    """

    class Meta:
        model = TodoItem

    title = factory.Faker('sentence', nb_words=5, variable_nb_words=True)
    description = factory.Faker('paragraph', nb_sentences=3,
                                variable_nb_sentences=True)
    due_date = timezone.now() + timedelta(days=7)
    todo_list = factory.SubFactory(TodoListFactory)
