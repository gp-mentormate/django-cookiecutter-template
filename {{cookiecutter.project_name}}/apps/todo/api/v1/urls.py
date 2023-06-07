# The `urls.py` file in Django contains the routing configuration for the app,
# mapping URLs to views and defining the URL patterns.
# Palace all url configurations related with the app here.
from rest_framework.routers import DefaultRouter

from apps.todo.api.v1.views import TodoListModelViewSet

urlpatterns = [
]

router = DefaultRouter()
router.register('', TodoListModelViewSet, basename='todo_list')
urlpatterns += router.urls
