from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

app_name = 'api-v1'
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
]
