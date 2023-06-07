from django.core import mail
from django.test import TestCase, tag
from faker import Faker

from apps.todo.api.v1.services import new_todo_list_email


@tag('emails', 'todo', 'todo-v1')
class EmailServiceTest(TestCase):
    def setUp(self):
        self.fake = Faker()

    def test_new_todo_list_email_success(self):
        # Arrange
        email = self.fake.email()

        # Act
        mail_is_sent = new_todo_list_email(recipients=[email])

        # Assert
        self.assertTrue(mail_is_sent)
        self.assertEqual(len(mail.outbox), 1)

        self.assertEqual(mail.outbox[0].subject, "New Todo List Created")

    def test_new_todo_list_email_failure(self):
        # Act
        mail_is_sent = new_todo_list_email(recipients=[self.fake.user_name()])

        # Assert
        self.assertFalse(mail_is_sent)
