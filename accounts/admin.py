from django.contrib import admin
from .models import Department, UserProfile


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "created_at",
    )

    search_fields = (
        "name",
    )

    ordering = (
        "name",
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "matricule",
        "department",
        "job_title",
        "is_active_employee",
    )

    list_filter = (
        "department",
        "is_active_employee",
    )

    search_fields = (
        "user__username",
        "user__first_name",
        "user__last_name",
        "matricule",
    )