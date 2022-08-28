from django.contrib import admin

from .models import User, Mentor, Student


admin.site.register(User)
admin.site.register(Mentor)
admin.site.register(Student)