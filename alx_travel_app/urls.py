from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger/OpenAPI documentation settings
schema_view = get_schema_view(
   openapi.Info(
      title="ALX Travel App API",
      default_version='v1',
      description="API for managing travel listings and bookings.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@travelapp.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # API endpoints
    path('api/', include('listings.urls')),

    # Documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]