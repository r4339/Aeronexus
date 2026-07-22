from django.contrib import admin
from .models import Permission


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "asset",
        "access_level",
        "status",
        "expiration_date",
        "granted_at",
    )

    list_filter = (
        "status",
        "access_level",
        "expiration_date",
    )

    search_fields = (
        "user__username",
        "asset__name",
    )

    ordering = (
        "-granted_at",
    )