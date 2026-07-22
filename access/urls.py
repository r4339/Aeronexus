from django.urls import path
from . import views

app_name = "access"

urlpatterns = [

    path(
        "",
        views.requests_list,
        name="requests_list"
    ),

    path(
        "create/",
        views.request_create,
        name="request_create"
    ),

    path(
        "<int:id>/",
        views.request_detail,
        name="request_detail"
    ),

    path(
        "<int:id>/update/",
        views.request_update,
        name="request_update"
    ),

    path(
        "<int:id>/delete/",
        views.request_delete,
        name="request_delete"
    ),

    path(
        "<int:id>/approve/",
        views.approve_request,
        name="approve_request"
    ),

    path(
        "<int:id>/reject/",
        views.reject_request,
        name="reject_request"
    ),

    path(
        "<int:id>/revoke/",
        views.revoke_request,
        name="revoke_request"
    ),

    path(
        "pending/",
        views.pending_requests,
        name="pending_requests"
    ),
        path(
        "approved/",
        views.approved_requests,
        name="approved_requests"
    ),

    path(
        "rejected/",
        views.rejected_requests,
        name="rejected_requests"
    ),

]