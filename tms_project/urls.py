from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from tasks.views import TaskViewSet  # Ensure this import is correct

# Initialize the router
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

# Swagger documentation setup
schema_view = get_schema_view(
    openapi.Info(
        title="Task Management API",
        default_version='v1',
    ),
    public=True,
    permission_classes=(AllowAny,),
)

# Define URL patterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),  # Include API routes
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Add Swagger
]
