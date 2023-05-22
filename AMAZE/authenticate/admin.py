from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class AmazeCustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {"fields": ("user_name", "email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "phone")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_seller",
                )
            },
        ),
        (("Dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "user_name",
                    "phone",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_seller",
                ),
            },
        ),
    )

    list_display = ("email", "phone", "user_name", "is_staff", "is_active", "is_seller")


admin.site.register(User, AmazeCustomUserAdmin)
