from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "action",
        "module",
        "created_at",
    )

    list_filter = (
        "action",
        "module",
        "created_at",
    )

    search_fields = (
        "user__username",
        "description",
        "module",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )