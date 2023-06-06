# The `serializers.py` file is responsible for defining serialization
# and deserialization logic to convert complex data types, such as
# model instances, into JSON or other formats for API responses and vice versa.
# Create your serializers here.

from rest_framework import serializers

from apps.todo.models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title')
        extra_kwargs = {
            'id': {'read_only': True},
        }
