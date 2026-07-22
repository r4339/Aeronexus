from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Asset, AssetAssignment
from .forms import (
    AssetForm,
    AssetAssignmentForm,
)
from .services import (
    AssetService,
    AssetAssignmentService,
)

@login_required
@permission_required(
    "assets.view_asset",
    raise_exception=True
)

def assets_list(request):

    assets = AssetService.get_all_assets()

    return render(
        request,
        "assets/assets_list.html",
        {
            "assets": assets,
        },
    )

@login_required
@permission_required(
    "assets.view_asset",
    raise_exception=True
)
def asset_detail(request, id):

    asset = AssetService.get_asset_by_id(id)

    return render(
        request,
        "assets/asset_detail.html",
        {
            "asset": asset,
        },
    )

@login_required
@permission_required(
    "assets.add_asset",
    raise_exception=True
)

def asset_create(request):

    if request.method == "POST":

        form = AssetForm(request.POST)

        if form.is_valid():

            AssetService.create_asset(form)

            messages.success(
                request,
                "Actif ajouté avec succès."
            )

            return redirect("assets:assets_list")

    else:

        form = AssetForm()

    return render(
        request,
        "assets/asset_create.html",
        {
            "form": form,
        },
    )

@login_required
@permission_required(
    "assets.change_asset",
    raise_exception=True
)

def asset_update(request, id):

    asset = get_object_or_404(
        Asset,
        id=id
    )

    if request.method == "POST":

        form = AssetForm(
            request.POST,
            instance=asset
        )

        if form.is_valid():

            AssetService.update_asset(form)

            messages.success(
                request,
                "Actif modifié avec succès."
            )

            return redirect("assets:assets_list")

    else:

        form = AssetForm(instance=asset)

    return render(
        request,
        "assets/asset_update.html",
        {
            "form": form,
            "asset": asset,
        },
    )

@login_required
@permission_required(
    "assets.delete_asset",
    raise_exception=True
)

def asset_delete(request, id):

    asset = get_object_or_404(
        Asset,
        id=id
    )

    AssetService.delete_asset(asset)

    messages.success(
        request,
        "Actif supprimé."
    )

    return redirect("assets:assets_list")

@login_required
@permission_required(
    "assets.view_assetassignement",
    raise_exception=True
)

def assignments_list(request):

    assignments = AssetAssignmentService.get_all_assignments()

    return render(
        request,
        "assets/assignments_list.html",
        {
            "assignments": assignments,
        },
    )

@login_required
@permission_required(
    "assets.add_assetassignment",
    raise_exception=True
)
def assign_asset(request):

    if request.method == "POST":

        form = AssetAssignmentForm(request.POST)

        if form.is_valid():

            AssetAssignmentService.assign_asset(form)

            messages.success(
                request,
                "Actif affecté avec succès."
            )

            return redirect("assets:assignments_list")

    else:

        form = AssetAssignmentForm()

    return render(
        request,
        "assets/assign_asset.html",
        {
            "form": form,
        },
    )

@login_required
@permission_required(
    "assets.change_assetassignment",
    raise_exception=True
)

def return_asset(request, id):

    assignment = get_object_or_404(
        AssetAssignment,
        id=id
    )

    AssetAssignmentService.return_asset(
        assignment
    )

    messages.success(
        request,
        "Actif retourné."
    )

    return redirect("assets:assignments_list")