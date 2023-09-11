from django.contrib import admin

from .models import (Project, ProjectFile, User, Mentor, Student, Article,
                     Subject, Project, ProjectFile, Response, Announcement)

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


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'created',
    ]
    list_filter = [
        'created',
        'modified',
    ]
    search_fields = [
        'title',
    ]
    readonly_fields = [
        'created',
        'modified',
    ]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created',
    ]
    list_filter = [
        'created',
        'modified',
    ]
    search_fields = [
        'name',
    ]
    readonly_fields = [
        'created',
        'modified',
    ]


class ProjectFileInline(admin.StackedInline):
    model = ProjectFile
    extra = 0
    readonly_fields = [
        'project_id',
    ]

class ResponseInline(admin.StackedInline):
    model = Response
    extra = 0
    readonly_fields = [
        'project_id',
        'student_id',
    ]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'subject',
        'created',
    ]
    list_filter = [
        'created',
        'modified',
    ]
    search_fields = [
        'title',
        'subject',
    ]
    readonly_fields = [
        'author',
        'implementer',
        'created',
        'modified',
    ]
    inlines = [ProjectFileInline, ResponseInline]


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'text',
        'venue',
        'date_venue',
    ]
    list_filter = [
        'type',
        'date_venue',
    ]
    readonly_fields = [
        'created',
        'modified',
    ]
