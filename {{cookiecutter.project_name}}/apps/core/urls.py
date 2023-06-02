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

urlpatterns = [
    # Django urls
    path('admin/', admin.site.urls),
    path('drf-auth/', include('rest_framework.urls')),

    # REST API urls

    # Documentation urls
    path('docs/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('docs/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, 'users')

urlpatterns += router.urls
