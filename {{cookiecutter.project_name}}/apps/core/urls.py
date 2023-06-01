# The `urls.py` file in Django is responsible for mapping URL patterns to
# corresponding views or endpoints within a Django project, allowing for
# proper routing and handling of incoming requests.
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
from rest_framework import routers, permissions

from apps.core.views import UserViewSet


app_name = 'core'

urlpatterns = [
    path('docs/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger-ui/', SpectacularSwaggerView.as_view(url_name='api:schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='api:schema'), name='redoc'),
]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')

urlpatterns += router.urls
