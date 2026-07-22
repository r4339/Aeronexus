from django.urls import path
from . import views

app_name = "compliance"

urlpatterns = [

    path(
        "",
        views.checks_list,
        name="checks_list"
    ),

    path(
        "<int:id>/",
        views.check_detail,
        name="check_detail"
    ),

    path(
        "compliant/",
        views.compliant_checks,
        name="compliant_checks"
    ),

    path(
        "warning/",
        views.warning_checks,
        name="warning_checks"
    ),

    path(
        "non-compliant/",
        views.non_compliant_checks,
        name="non_compliant_checks"
    ),

]