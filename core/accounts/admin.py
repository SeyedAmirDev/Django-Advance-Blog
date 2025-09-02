from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Profile


User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("email", "is_staff", "is_superuser", "is_active")
    search_fields = ("email", )
    list_filter = ("is_staff", "is_superuser", "is_active")
    ordering = ("email",)

    fieldsets = (
        (_('Authentication'), {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (
            _('Group Permissions'),
            {
                "fields": (
                    "groups",
                    "user_permissions",
                )
            }
        ),
        (_("Important dates"), {"fields": ("last_login", "created_date", "updated_date")}),
    )
    readonly_fields = ("last_login", "created_date", "updated_date")

    add_fieldsets = (
        (
            _('Add User'),
            {
                "classes": ("wide",),
                "fields": ("email", "is_staff", "is_active", "is_superuser",
                           "password1", "password2"),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "pk", "first_name", "last_name", "get_user_email"
    )
    search_fields = ("first_name", "last_name")

    fieldsets = (
        (_('Profile Info'), {"fields": (
            "user",
            "first_name",
            "last_name",
            "image",
            "description"
        )}),
        (_("Important dates"), {"fields": ("created_date", "updated_date")}),
    )

    readonly_fields = ("created_date", "updated_date")

    add_fieldsets = (
        (
            _('Add Profile'),
            {
                "classes": ("wide",),
                "fields": (
                    "user",
                    "first_name",
                    "last_name",
                    "image",
                    "description"
                )
            },
        ),
    )

    def get_user_email(self, instance):
        return instance.user.email

    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)
