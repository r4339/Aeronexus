from django.urls import path
from . import views

app_name = "assets"

urlpatterns = [

    path(
        "",
        views.assets_list,
        name="assets_list"
    ),

    path(
        "create/",
        views.asset_create,
        name="asset_create"
    ),

    path(
        "<int:id>/",
        views.asset_detail,
        name="asset_detail"
    ),

    path(
        "<int:id>/update/",
        views.asset_update,
        name="asset_update"
    ),

    path(
        "<int:id>/delete/",
        views.asset_delete,
        name="asset_delete"
    ),

    path(
        "assignments/",
        views.assignments_list,
        name="assignments_list"
    ),

    path(
        "assignments/create/",
        views.assign_asset,
        name="assign_asset"
    ),

    path(
        "assignments/<int:id>/return/",
        views.return_asset,
        name="return_asset"
    ),

]