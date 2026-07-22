from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [

    path(
        "",
        views.users_list,
        name="users_list"
    ),

    path(
        "create/",
        views.user_create,
        name="user_create"
    ),

    path(
        "<int:id>/",
        views.user_detail,
        name="user_detail"
    ),

    path(
        "<int:id>/update/",
        views.user_update,
        name="user_update"
    ),

    path(
        "<int:id>/toggle/",
        views.toggle_user_status,
        name="toggle_user_status"
    ),

    path(
        "login/",
        views.login_view,
        name="login"
    ),

    path(
        "logout/",
        views.logout_view,
        name="logout"
    ),

    path(
        "profile/",
        views.my_profile,
        name="my_profile"
    ),

]
