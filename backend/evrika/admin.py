from django.contrib import admin

from .models import User, Mentor, Student, Publication, PublicationImage, Document


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