from django.contrib import admin
from .models import SaveDbConsulting, SaveDbCalculating, SaveDbReview


@admin.register(SaveDbConsulting)
class SaveDbConsultingAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer_name', 'phone_number', 'description']
    list_display_links = ['id', 'buyer_name']
    search_fields = ['buyer_name', 'phone_number', 'description']
    list_filter = ['buyer_name']
    list_per_page = 20

    def __str__(self):
        return "Consults"


@admin.register(SaveDbCalculating)
class SaveDbCalculatingAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer_name', 'phone_number', 'room_type', 'company_name', 'room_area', 'created_at']
    list_display_links = ['id', 'buyer_name']
    search_fields = ['buyer_name', 'phone_number', 'company_name', 'room_type']
    list_filter = ['room_type', 'created_at']
    readonly_fields = ['created_at']  # нельзя редактировать
    list_per_page = 20

    def __str__(self):
        return "Calculating Consults"


@admin.register(SaveDbReview)
class SaveDbReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'buyer_name', 'phone_number', 'rate', 'description_short']
    list_display_links = ['id', 'buyer_name']
    search_fields = ['buyer_name', 'phone_number', 'description']
    list_filter = ['rate']
    list_per_page = 20

    def description_short(self, obj):
        """Сокращенное описание для списка"""
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description

    description_short.short_description = 'Описание'

    def __str__(self):
        return "Reviews"