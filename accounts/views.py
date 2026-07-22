from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)
from django.contrib import messages

from .models import UserProfile
from .forms import UserForm,UserUpdateForm, UserProfileForm
from .services import UserService


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("accounts:users_list")

        messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")

    return render(request, "login.html")


@login_required
def logout_view(request):
    logout(request)

    return redirect("accounts:login")


@login_required
def my_profile(request):
    profile = UserProfile.objects.filter(user=request.user).select_related(
        "department"
    ).first()
    return render(request, "accounts/my_profile.html", {"profile": profile})

@login_required
@permission_required(
    "accounts.view_userprofile",
    raise_exception=True
)

def users_list(request):

    users = UserService.get_all_users()

    return render(
        request,
        "accounts/users_list.html",
        {
            "users": users
        }
    )

@login_required
@permission_required(
    "accounts.view_userprofile",
    raise_exception=True
)

def user_detail(request, id):

    profile = UserService.get_user(id)

    return render(
        request,
        "accounts/user_detail.html",
        {
            "profile": profile
        }
    )

@login_required
@permission_required(
    "accounts.add_userprofile",
    raise_exception=True
)

def user_create(request):

    if request.method == "POST":

        user_form = UserForm(request.POST)

        profile_form = UserProfileForm(
            request.POST,
            request.FILES
        )

        if user_form.is_valid() and profile_form.is_valid():

           user = user_form.save(commit=False)

           user.set_password(
           user_form.cleaned_data["password"]
           ) 
           user.save()

           profile = profile_form.save(commit=False)
           profile.user = user
           profile.save()

        messages.success(
                request,
                "Utilisateur créé avec succès."
            )

        return redirect("accounts:users_list")

    else:

        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(
        request,
        "accounts/user_create.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        }
    )

@login_required
@permission_required(
    "accounts.change_userprofile",
    raise_exception=True
)

def user_update(request, id):

    profile = get_object_or_404(
        UserProfile,
        id=id
    )

    if request.method == "POST":

      user_form = UserUpdateForm(
       request.POST,
       instance=profile.user
      )

      profile_form = UserProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

      if user_form.is_valid() and profile_form.is_valid():

            user_form.save()
            profile_form.save()

            messages.success(
                request,
                "Utilisateur modifié avec succès."
            )

            return redirect("accounts:users_list")

    else:

        user_form = UserUpdateForm(instance=profile.user)
        profile_form = UserProfileForm(instance=profile)

    return render(
        request,
        "accounts/user_update.html",
        {
            "user_form": user_form,
            "profile_form": profile_form,
        }
    )

@login_required
@permission_required(
    "accounts.change_userprofile",
    raise_exception=True
)

def toggle_user_status(request, id):

        profile = get_object_or_404(
        UserProfile,
        id=id
        )

        UserService.toggle_status(profile)

        messages.success(
        request,
        "Statut de l'utilisateur mis à jour."
         )

        return redirect("accounts:dashboard:index")
