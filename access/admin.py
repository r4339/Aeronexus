from django.contrib import admin
from .models import AccessRequest


@admin.register(AccessRequest)
class AccessRequestAdmin(admin.ModelAdmin):

    list_display = (
        "requester",
        "asset",
        "access_level",
        "status",
        "start_date",
        "end_date",
        "created_at",
    )

    list_filter = (
        "status",
        "access_level",
        "start_date",
    )

    search_fields = (
        "requester__username",
        "asset__name",
    )

    ordering = (
        "-created_at",
    )