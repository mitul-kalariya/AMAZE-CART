from django.contrib import admin
from customer.models import customer
from django.contrib.auth.admin import UserAdmin


# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             "Extra info",
#             {"fields": ("dob", "gender", "phone")},
#         ),
#     )
# admin.site.register(customer, CustomUserAdmin)


# Register your models here.
fields = list(UserAdmin.fieldsets)
fields[1] = (
    "Personal Info",
    {"fields": ("first_name", "last_name", "email", "dob", "gender", "phone")},
)
UserAdmin.fieldsets = tuple(fields)
admin.site.register(customer, UserAdmin)
