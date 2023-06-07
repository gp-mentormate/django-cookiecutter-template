# The `serializers.py` file is responsible for defining serialization
# and deserialization logic to convert complex data types, such as
# model instances, into JSON or other formats for API responses and vice versa.
# Create your services here.
import logging
from typing import Union

from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db.models import QuerySet
from email_from_template import send_mail

from apps.todo.api.v1.selectors import all_todo_lists, user_todo_lists
from config.settings.local import ADMINS


def get_todo_lists(*, user: Union[AbstractUser, AnonymousUser]) -> QuerySet:
    """
    Retrieves the todo lists based on the user.

    Args:
        user (Union[AbstractUser, AnonymousUser]): The user for whom to
                                                   retrieve the todo lists.
                                                   It can be an instance of
                                                   AbstractUser (authenticated user)
                                                   or AnonymousUser (unauthenticated user).

    Returns:
        QuerySet: A Django QuerySet containing the todo lists.

    Raises:
        None
    """
    if user.is_superuser:
        return all_todo_lists()
    elif user.is_authenticated:
        return user_todo_lists(user=user)
    else:
        return QuerySet.none()


def new_todo_list_email(*, recipients: list = None) -> bool:
    """
    Sends an email notification when a new todo list is created.

    Args:
        recipients (list, optional): A list of email addresses to
                                     send the notification to.
                                     If not provided, no emails will be sent.
                                     Default is None.

    Returns:
        bool: True if the email was sent successfully, False otherwise.

    Raises:
        None
    """

    if recipients is None:
        recipients = []

    if recipients:
        email_validator = EmailValidator()
        for email in recipients:
            try:
                email_validator(email)
            except ValidationError as e:
                logging.error(f"Invalid email address: {email} - {e}")
                return False

    try:
        send_mail(
            recipient_list=recipients,
            template="emails/v1/new_todo_list.email",
            context={},
            bcc=ADMINS,
            cc=[]
        )
    except Exception as e:
        logging.error(e)
        return False

    return True
