from django.contrib import admin
from .models import (
    AssetCategory,
    Asset,
    AssetAssignment,
    AssetDocument
)


@admin.register(AssetCategory)
class AssetCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "created_at",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):

    list_display = (
        "asset_code",
        "name",
        "category",
        "owner",
        "location",
        "criticality",
        "status",
    )

    list_filter = (
        "category",
        "criticality",
        "status",
    )

    search_fields = (
        "asset_code",
        "name",
        "location",
    )

    ordering = (
        "asset_code",
    )


@admin.register(AssetAssignment)
class AssetAssignmentAdmin(admin.ModelAdmin):

    list_display = (
        "asset",
        "user",
        "assigned_at",
        "returned_at",
        "active",
    )

    list_filter = (
        "active",
    )

    search_fields = (
        "asset__name",
        "user__username",
    )

    ordering = (
        "-assigned_at",
    )


@admin.register(AssetDocument)
class AssetDocumentAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "asset",
        "uploaded_at",
    )

    search_fields = (
        "title",
        "asset__name",
    )

    ordering = (
        "-uploaded_at",
    )