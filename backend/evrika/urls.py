from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
]
