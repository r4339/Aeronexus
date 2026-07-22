from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("reports/", views.reports, name="reports"),
    path("settings/", views.settings, name="settings"),
]
