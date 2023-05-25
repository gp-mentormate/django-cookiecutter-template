# The `apps.py` file in Django is responsible for application configuration
# and customization within a Django project. It provides the AppConfig class,
# which allows developers to customize the behavior of their applications.
# By subclassing AppConfig, developers can handle signals, define application
# labels, and perform initialization tasks, making it a crucial
# component for configuring Django applications.

from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'
