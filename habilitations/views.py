from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from django.contrib import messages

from .models import Permission
from .forms import PermissionForm
from .services import PermissionService


@login_required
@permission_required(
    "habilitations.view_permission",
    raise_exception=True
)
def permissions_list(request):

    permissions = PermissionService.get_all_permissions()

    return render(
        request,
        "habilitations/permissions_list.html",
        {
            "permissions": permissions
        }
    )


@login_required
@permission_required(
    "habilitations.view_permission",
    raise_exception=True
)
def permission_detail(request, id):

    permission = PermissionService.get_permission(id)

    return render(
        request,
        "habilitations/permission_detail.html",
        {
            "permission": permission
        }
    )


@login_required
@permission_required(
    "habilitations.change_permission",
    raise_exception=True
)
def permission_update(request, id):

    permission = get_object_or_404(
        Permission,
        id=id
    )

    if request.method == "POST":

        form = PermissionForm(
            request.POST,
            instance=permission
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Habilitation mise à jour avec succès."
            )

            return redirect(
                "habilitations:permissions_list"
            )

    else:

        form = PermissionForm(
            instance=permission
        )

    return render(
        request,
        "habilitations/permission_update.html",
        {
            "form": form,
            "permission": permission
        }
    )

@login_required
@permission_required(
    "habilitations.delete_permission",
    raise_exception=True
)
def permission_delete(request, id):

    permission = get_object_or_404(
        Permission,
        id=id
    )

    if request.method == "POST":

        permission.delete()

        messages.success(
            request,
            "Habilitation supprimée."
        )

        return redirect(
            "habilitations:permissions_list"
        )

    return render(
        request,
        "habilitations/permission_delete.html",
        {
            "permission": permission
        }
    )


@login_required
def revoke_permission(request, id):

    if not request.user.has_perm(
        "habilitations.revoke_permission"
    ):

        messages.error(
            request,
            "Vous n'avez pas la permission de révoquer une habilitation."
        )

        return redirect(
            "habilitations:permissions_list"
        )

    permission = get_object_or_404(
        Permission,
        id=id
    )

    PermissionService.revoke(
        permission,
        "Révoquée par un administrateur."
    )

    messages.warning(
        request,
        "Habilitation révoquée."
    )

    return redirect(
        "habilitations:permissions_list"
    )


@login_required
@permission_required(
    "habilitations.view_permission",
    raise_exception=True
)
def expired_permissions(request):

    permissions = PermissionService.expired_permissions()

    return render(
        request,
        "habilitations/expired_permissions.html",
        {
            "permissions": permissions
        }
    )

@login_required
@permission_required(
    "habilitations.view_permission",
    raise_exception=True
)
def revoked_permissions(request):

    permissions = PermissionService.revoked_permissions()

    return render(
        request,
        "habilitations/revoked_permissions.html",
        {
            "permissions": permissions
        }
    )