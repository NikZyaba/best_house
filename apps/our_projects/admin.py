from django.contrib import admin
from .models import OurProjects


@admin.register(OurProjects)
class OurProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'project_description']  # что показывать в списке
    list_display_links = ['id', 'project_description']  # кликабельные поля
    search_fields = ['project_description']  # поля для поиска

    fieldsets = [
        (None, {
            'fields': ['project_image', 'project_description']
        }),
    ]