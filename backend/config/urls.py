"""Main file of URL dispatcher"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^login/$', obtain_jwt_token),
    path('api/v1/', include('evrika.urls', namespace='apiv1')),
]
