# The `views.py` file in Django contains the logic for handling HTTP requests,
# processing data, and rendering the appropriate response, serving as the
# bridge between the user's interactions and the application's business logic.
# Create your views here.
import logging
from typing import Any

from email_from_template import send_mail
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.todo.api.v1.serializers import TodoListSerializer
from apps.todo.api.v1.services import get_todo_lists
from apps.todo.models import TodoList
from config.settings.base import ADMINS


class TodoListModelViewSet(ModelViewSet):
    """
    This ViewSet provides CRUD (Create, Retrieve, Update, Delete) operations for TodoLists.
    """

    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()

    def get_queryset(self):
        return get_todo_lists(user=self.request.user)
