from django import forms
from django.contrib.auth.models import User
from .models import Department, UserProfile


class UserForm(forms.ModelForm):

    password = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput()
    )

    confirm_password = forms.CharField(
        label="Confirmer le mot de passe",
        widget=forms.PasswordInput()
    )
class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User

        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
        ]

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password and confirm and password != confirm:
            raise forms.ValidationError(
                "Les mots de passe ne correspondent pas."
            )

        return cleaned_data

class UserProfileForm(forms.ModelForm):

    class Meta:

        model = UserProfile

        fields = [
            "matricule",
            "phone",
            "department",
            "job_title",
            "photo",
            "is_active_employee",
        ]


class DepartmentForm(forms.ModelForm):

    class Meta:

        model = Department

        fields = "__all__"