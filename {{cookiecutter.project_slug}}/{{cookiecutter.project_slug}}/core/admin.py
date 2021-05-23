from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.

admin.site.register(Permission)


@admin.register(User)
class UserDisplay(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
    )
    search_fields = (
        "id",
        "email",
        "first_name",
        "last_name",
    )
