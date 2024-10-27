from django.contrib import admin

from accounts.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'can_post', 'has_access', 'is_active', 'verify_date')
    list_display_links = list_display
    search_fields = ('email',)
