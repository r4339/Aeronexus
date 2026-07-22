from django import forms
from .models import AuditLog


class AuditLogForm(forms.ModelForm):

    class Meta:

        model = AuditLog

        fields = [
            "action",
            "module",
            "description",
        ]

        widgets = {

            "description": forms.Textarea(
                attrs={
                    "rows": 4
                }
            )

        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs["class"] = "form-control"