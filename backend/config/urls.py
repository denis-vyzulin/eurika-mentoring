"""Main file of URL dispatcher"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('evrika.urls'), name="evrika"),
]