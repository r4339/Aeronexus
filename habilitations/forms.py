from django import forms
from .models import Permission


class PermissionForm(forms.ModelForm):

    class Meta:

        model = Permission

        fields = [

            "expiration_date",

            "status",

            "revoke_reason",

        ]

        widgets = {

            "expiration_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "revoke_reason": forms.Textarea(
                attrs={
                    "rows": 3
                }
            ),

        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs["class"] = "form-control"