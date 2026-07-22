from django.urls import path
from . import views

app_name = "audit"

urlpatterns = [

    path(
        "",
        views.logs_list,
        name="logs_list"
    ),

    path(
        "<int:id>/",
        views.log_detail,
        name="log_detail"
    ),

    path(
        "module/<str:module>/",
        views.logs_by_module,
        name="logs_by_module"
    ),

    path(
        "action/<str:action>/",
        views.logs_by_action,
        name="logs_by_action"
    ),

]