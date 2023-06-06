# The `urls.py` file in Django contains the routing configuration for the app,
# mapping URLs to views and defining the URL patterns.
# Palace all main url configurations related with the project here.

from django.contrib import admin
from django.urls import (
    include,
    path,
)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)
from rest_framework import routers

from apps.core.views import UserViewSet

{%- if cookiecutter.add_example_api == 'True' %}

urlpatterns_api_v1 = [
    path('auth/', include('apps.auth.api.v1.urls'))
]

{%- endif %}

urlpatterns = [
    # Django urls
    path('admin/', admin.site.urls),
    path('drf-auth/', include('rest_framework.urls')),

    # REST API urls
    {%- if cookiecutter.add_example_api == 'True' %}
    path('api/v1/', include(urlpatterns_api_v1)),

    {% endif -%}

    # Documentation urls
    path('docs/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')

urlpatterns += router.urls
