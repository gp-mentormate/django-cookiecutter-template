from django.test import tag
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from apps.todo.factories import TodoListFactory
from apps.users.factories import CustomUserFactory


@tag('api', 'api-v1', 'todo', 'todo-v1')
class TodoListListTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUserFactory()
        self.todo_list = TodoListFactory(created_by=self.user)

    def test_get_todo_lists(self):
        # Arrange
        # The authentication should be covered by own tests.
        # Here we're using the build-in force authentication functionality.
        self.client.force_authenticate(user=self.user)

        # Act
        response = self.client.get(reverse('todo_list-list'))

        # Assert
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.todo_list.id)

    def test_get_todo_lists_forbidden(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('todo_list-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_todo_lists_unauthorized(self):
        # Arrange
        not_owner = CustomUserFactory()
        self.client.force_authenticate(user=not_owner)

        # Act
        response = self.client.get(
            reverse('todo_list-detail', kwargs={'pk': self.todo_list.id})
        )

        # Assert
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
