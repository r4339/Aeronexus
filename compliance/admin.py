from django.contrib import admin
from .models import ComplianceCheck


@admin.register(ComplianceCheck)
class ComplianceCheckAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "status",
        "checked_at",
    )

    list_filter = (
        "status",
        "checked_at",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "-checked_at",
    )

    readonly_fields = (
        "checked_at",
    )