from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST

from .models import AccessRequest
from .forms import AccessRequestForm
from .services import AccessRequestService


def _can_manage_access_requests(user):
    """Only platform administrators may make an access decision."""
    return user.is_superuser or user.groups.filter(name="Administrateur").exists()


@login_required
@permission_required(
    "access.view_accessrequest",
    raise_exception=True
)
def requests_list(request):

    requests = AccessRequestService.get_all_requests()

    return render(
        request,
        "access/access_list.html",
        {
            "requests": requests,
            "can_manage_access_requests": _can_manage_access_requests(request.user),
        }
    )


@login_required
@permission_required(
    "access.view_accessrequest",
    raise_exception=True
)
def request_detail(request, id):

    access_request = AccessRequestService.get_request(id)

    return render(
        request,
        "access/access_detail.html",
        {
            "access_request": access_request
        }
    )


@login_required
@permission_required(
    "access.add_accessrequest",
    raise_exception=True
)
def request_create(request):

    if request.method == "POST":

        form = AccessRequestForm(request.POST)

        if form.is_valid():

            AccessRequestService.create_request(
                form,
                request.user
            )

            messages.success(
                request,
                "La demande d'accès a été créée avec succès."
            )

            return redirect(
                "access:requests_list"
            )

    else:

        form = AccessRequestForm()

    return render(
        request,
        "access/access_create.html",
        {
            "form": form
        }
    )


@login_required
@permission_required(
    "access.change_accessrequest",
    raise_exception=True
)
def request_update(request, id):

    access_request = get_object_or_404(
        AccessRequest,
        id=id
    )

    if request.method == "POST":

        form = AccessRequestForm(
            request.POST,
            instance=access_request
        )

        if form.is_valid():

            AccessRequestService.update_request(form)

            messages.success(
                request,
                "La demande a été modifiée."
            )

            return redirect(
                "access:requests_list"
            )

    else:

        form = AccessRequestForm(
            instance=access_request
        )

    return render(
        request,
        "access/access_update.html",
        {
            "form": form,
            "access_request": access_request
        }
    )


@login_required
@permission_required(
    "access.delete_accessrequest",
    raise_exception=True
)
def request_delete(request, id):

    access_request = get_object_or_404(
    AccessRequest,
    pk=id
)

    if request.method == "POST":

        AccessRequestService.delete_request(
            access_request
        )

        messages.success(
            request,
            "La demande a été supprimée."
        )

        return redirect(
            "access:requests_list"
        )

    return render(
        request,
        "access/access_delete.html",
        {
            "access_request": access_request
        }
    )


@login_required
@require_POST
def approve_request(request, id):

    if not _can_manage_access_requests(request.user):
        raise PermissionDenied

    access_request = get_object_or_404(
    AccessRequest,
    pk=id
)

    if access_request.status == "PENDING":

        AccessRequestService.manager_approve(
            access_request,
            request.user
        )

        messages.success(
            request,
            "Demande validée par le responsable."
        )

    elif access_request.status == "MANAGER_APPROVED":

        AccessRequestService.rssi_approve(
            access_request,
            request.user
        )

        messages.success(
            request,
            "Demande validée par le RSSI."
        )

    return redirect("access:requests_list")
@login_required
@require_POST
def reject_request(request, id):

    if not _can_manage_access_requests(request.user):
        raise PermissionDenied

    access_request = get_object_or_404(
    AccessRequest,
    pk=id
)

    comment = "Demande refusée"

    if access_request.status == "PENDING":

        AccessRequestService.manager_reject(
            access_request,
            request.user,
            comment
        )

        messages.error(
            request,
            "Demande refusée par le responsable."
        )

    elif access_request.status == "MANAGER_APPROVED":

        AccessRequestService.rssi_reject(
            access_request,
            request.user,
            comment
        )

        messages.error(
            request,
            "Demande refusée par le RSSI."
        )

    return redirect("access:requests_list")
@login_required
@permission_required(
    "access.revoke_accessrequest",
    raise_exception=True
)
def revoke_request(request, id):

    if not request.user.has_perm(
        "access.revoke_access"
    ):

        messages.error(
            request,
            "Vous n'avez pas cette permission."
        )

        return redirect(
            "access:requests_list"
        )


@login_required
@permission_required(
    "access.view_accessrequest",
    raise_exception=True
)
def pending_requests(request):

    requests = AccessRequestService.pending_requests()

    return render(
        request,
        "access/pending_requests.html",
        {
            "requests": requests,
            "can_manage_access_requests": _can_manage_access_requests(request.user),
        }
    )
@login_required
@permission_required(
    "access.approve_accessrequest",
    raise_exception=True
)
def approved_requests(request):

    requests = AccessRequestService.approved_requests()

    return render(
        request,
        "access/approved_requests.html",
        {
            "requests": requests
        }
    )


@login_required
@permission_required(
    "access.reject_accessrequest",
    raise_exception=True
)
def rejected_requests(request):

    requests = AccessRequestService.rejected_requests()

    return render(
        request,
        "access/rejected_requests.html",
        {
            "requests": requests
        }
    )
