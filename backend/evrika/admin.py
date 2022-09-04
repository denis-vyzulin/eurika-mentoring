from django.contrib import admin

from .models import (Project, ProjectFile, User, Mentor, Student, Publication,
                PublicationImage, Document, Direction, Project, ProjectFile,
                ProjectStudent)

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


class PublicationImageInline(admin.StackedInline):
    model = PublicationImage
    extra = 0

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
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
    inlines = [PublicationImageInline]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'created',
        'modified',
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


class DirectionAdmin(admin.ModelAdmin):
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

class ProjectStudentInline(admin.StackedInline):
    model = ProjectStudent
    extra = 0
    readonly_fields = [
        'student',
    ]

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'direction',
        'created',
    ]
    list_filter = [
        'created',
        'modified',
    ]
    search_fields = [
        'title',
        'direction',
    ]
    readonly_fields = [
        'created',
        'modified',
    ]
    inlines = [ProjectFileInline, ProjectStudentInline]