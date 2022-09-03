from django.contrib import admin

from .models import User, Mentor, Student


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'username',
        'surname',
        'is_active',
        'is_staff',
    ]
    list_filter = [
        'is_active',
        'is_staff'
    ]
    ordering = ['-is_active', '-date_joined', 'username']


admin.site.register(User, UserAdmin)
admin.site.register(Mentor, UserAdmin)
admin.site.register(Student, UserAdmin)