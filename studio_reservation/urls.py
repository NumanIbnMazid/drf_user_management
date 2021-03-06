# imports
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from utils.decorators import has_staff_permission_required


# Define Rest Framework Router
router = DefaultRouter()

# Swagger Schema
schema_view = get_schema_view(
    openapi.Info(
        title="Studio Reservation System API",
        default_version='v1',
        description="Studio Reservation System API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="numanibnmazid@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

""" Third Party URL Patterns """
THIRD_PARTY_URL_PATTERNS = [
    # Django Rest Framework
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Django Rest Auth
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    # Django Rest Framework JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Yet Another Swagger
    url(r'^swagger(?P<format>\.json|\.yaml)$', has_staff_permission_required(schema_view.without_ui(cache_timeout=0)), name='schema-json'),
    url(r'^swagger/$', has_staff_permission_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    url(r'^redoc/$', has_staff_permission_required(schema_view.with_ui('redoc', cache_timeout=0)), name='schema-redoc'),
]

INTERNAL_APP_URL_PATTERNS = [
    # ==============================*** CUSTOMER URLS ***==============================
    path("customer/", include(("customers.api.urls", "customers"), namespace="customers")),
    path("staff/", include(("staffs.api.urls", "staffs"), namespace="staffs")),
]

""" URL Patterns - Main """
urlpatterns = [
    path('admin/', admin.site.urls),
] + THIRD_PARTY_URL_PATTERNS + INTERNAL_APP_URL_PATTERNS

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
