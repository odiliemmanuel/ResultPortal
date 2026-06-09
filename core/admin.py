from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("first_name","last_name","email","last_login")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "username")}),
        (
            "Permissions", {
                "fields": ("is_active", "is_staff", "is_superuser", "role", "groups", "user_permissions"),
            }),
        ("Important dates", {"fields": ("last_login", "created_at", "updated_at")}),
    )

    add_fieldsets = (
        (None, {

            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "role", "username","password"),
        }),
    )
    search_fields = ("username", "email","first_name", "last_name")
    ordering = ("created_at",)
    readonly_fields = ('created_at', 'updated_at')