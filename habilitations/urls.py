from django.urls import path
from . import views

app_name = "habilitations"

urlpatterns = [

    path(
        "",
        views.permissions_list,
        name="permissions_list"
    ),

    path(
        "<int:id>/",
        views.permission_detail,
        name="permission_detail"
    ),

    path(
        "<int:id>/update/",
        views.permission_update,
        name="permission_update"
    ),

    path(
        "<int:id>/delete/",
        views.permission_delete,
        name="permission_delete"
    ),

    path(
        "<int:id>/revoke/",
        views.revoke_permission,
        name="revoke_permission"
    ),

    path(
        "expired/",
        views.expired_permissions,
        name="expired_permissions"
    ),

    path(
        "revoked/",
        views.revoked_permissions,
        name="revoked_permissions"
    ),

]