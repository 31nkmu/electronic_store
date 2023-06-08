from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_seller', 'is_active']


admin.site.register(User, UserAdmin)