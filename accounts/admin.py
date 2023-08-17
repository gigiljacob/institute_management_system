from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.forms import ImsUserCreationForm, ImsUserChangeForm
from accounts.models import ImsUser


@admin.register(ImsUser)
class ImsUserAdmin(UserAdmin):
    add_form = ImsUserCreationForm
    form = ImsUserChangeForm
    model = ImsUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
         ),
    )
    search_fields = ("email",)
    ordering = ("email",)
