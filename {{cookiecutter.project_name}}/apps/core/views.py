# The `views.py` file in Django contains the logic for handling HTTP requests,
# processing data, and rendering the appropriate response, serving as the
# bridge between the user's interactions and the application's business logic.

from apps.core.serializers import UserSerializer
from apps.core.services import get_all_users
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return get_all_users()
