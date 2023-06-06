from django.utils import timezone

from django.db import models
from django.urls import reverse

from apps.core.models import BaseModel


def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)


class TodoList(BaseModel):
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    def __str__(self):
        return self.title


class TodoItem(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
