from django import forms
from .models import ComplianceCheck


class ComplianceCheckForm(forms.ModelForm):

    class Meta:

        model = ComplianceCheck

        fields = [

            "name",

            "description",

            "status",

            "recommendation",

        ]

        widgets = {

            "description": forms.Textarea(
                attrs={
                    "rows": 4
                }
            ),

            "recommendation": forms.Textarea(
                attrs={
                    "rows": 4
                }
            ),

        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs["class"] = "form-control"