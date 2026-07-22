from django import forms

from .models import (
    AssetCategory,
    Asset,
    AssetAssignment,
    AssetDocument
)


class AssetCategoryForm(forms.ModelForm):

    class Meta:

        model = AssetCategory

        fields = [
            "name",
            "description",
        ]


class AssetForm(forms.ModelForm):

    class Meta:

        model = Asset

        fields = [
            "asset_code",
            "name",
            "category",
            "description",
            "owner",
            "location",
            "criticality",
            "status",
            "confidentiality",
            "integrity",
            "availability",
        ]


class AssetAssignmentForm(forms.ModelForm):

    class Meta:

        model = AssetAssignment

        fields = [
            "asset",
            "user",
            "returned_at",
            "active",
        ]


class AssetDocumentForm(forms.ModelForm):

    class Meta:

        model = AssetDocument

        fields = [
            "asset",
            "title",
            "file",
        ]