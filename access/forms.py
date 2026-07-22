from django import forms
from .models import AccessRequest


class AccessRequestForm(forms.ModelForm):

    class Meta:

        model = AccessRequest

        fields = [

            "asset",

            "access_level",

            "justification",

            "manager",

            "start_date",

            "end_date",

        ]

        widgets = {

            "justification": forms.Textarea(
                attrs={
                    "rows": 4
                }
            ),

            "start_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "end_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs["class"] = "form-control"