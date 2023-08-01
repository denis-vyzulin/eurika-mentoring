from django.contrib import admin

from .models import (User, Mentor, Student, Article, Subject,
                     Project, ProjectFile, Response, Announcement, University, School)
from .admin_user import UserMentorAdmin, UserStudentAdmin


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ['name']


class UserCustomAdmin(admin.ModelAdmin):
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

admin.site.register(User, UserCustomAdmin)


@admin.register(Mentor)
class MentorAdmin(UserMentorAdmin):
    list_display = [
        'email',
        'username',
        'patronymic',
        'surname',
        'university_id'
    ]
    ordering = ['-date_joined', 'username']
    readonly_fields = ['date_joined', 'last_login']


@admin.register(Student)
class StudentAdmin(UserStudentAdmin):
    list_display = [
        'email',
        'username',
        'patronymic',
        'surname',
        'get_school',
        'class_num'
    ]
    search_fields = ['email', 'surname']
    list_filter = ['class_num', 'school_id__name']
    ordering = ['-date_joined', 'username']
    readonly_fields = ['date_joined', 'last_login']

    def get_school(self, obj):
        return obj.school_id.name

    get_school.short_description = 'School'


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'type'
    ]
    list_filter = ['type']
    search_fields = [
        'title',
    ]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
    search_fields = [
        'name',
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
    ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'subject',
        'is_display',
        'is_complete',
        'author',
        'implementer'
    ]
    list_filter = [
        'is_display',
        'is_complete'
    ]
    search_fields = [
        'title',
        'subject',
        'description'
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
    search_fields = ['text']
