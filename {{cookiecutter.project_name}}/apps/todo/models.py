from django.db import models
from django.urls import reverse
from django.utils import timezone

from apps.core.models import BaseModel


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class TodoList(BaseModel):
    """
    TodoList class represents a todo list.

    This class extends the BaseModel class and provides
    functionality for managing todo lists.
    """
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self) -> str:
        """
        Return the absolute URL for the todo list.
        """
        return reverse("list", args=[self.id])

    def __str__(self) -> str:
        return self.title


class TodoItem(BaseModel):
    """
    TodoItem class represents a todo item.

    This class extends the BaseModel class
    and provides functionality for managing todo items.
    """

    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def get_absolute_url(self) -> str:
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self) -> str:
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
