from django.contrib import admin
from .models import (
    UserProfile,
)

# admin.site.register(UserProfile) # modelni adminda ko'rinishi
@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    """User admin, Accaunt"""
    list_display = ("id", "full_name","email", "gender", "active", "staff","admin")
    list_display_links = ("full_name",)