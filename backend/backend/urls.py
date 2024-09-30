from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

# backend/backend/settings.py
# Add 'tasks' and 'rest_framework' to INSTALLED_APPS
INSTALLED_APPS = [
    # ...
    'tasks',
    'rest_framework',
    'corsheaders',
]

# Add corsheaders middleware
MIDDLEWARE = [
    # ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]

# Allow all origins for development (customize for production)
CORS_ALLOW_ALL_ORIGINS = True
