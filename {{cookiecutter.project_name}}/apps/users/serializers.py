# The `serializers.py` file is responsible for defining serialization
# and deserialization logic to convert complex data types, such as
# model instances, into JSON or other formats for API responses and vice versa.

from models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'is_staff']
