from django.db import models
from django.contrib.auth.models import User


class AssetCategory(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.name
class Asset(models.Model):

    CRITICALITY_CHOICES = [

        ("LOW", "Faible"),
        ("MEDIUM", "Moyenne"),
        ("HIGH", "Élevée"),
        ("CRITICAL", "Critique"),

    ]

    STATUS_CHOICES = [

        ("ACTIVE", "Actif"),
        ("MAINTENANCE", "Maintenance"),
        ("RETIRED", "Retiré"),

    ]

    asset_code = models.CharField(
        max_length=50,
        unique=True
    )

    name = models.CharField(
        max_length=150
    )

    category = models.ForeignKey(
        AssetCategory,
        on_delete=models.PROTECT,
        related_name="assets"
    )

    description = models.TextField(
        blank=True
    )

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    location = models.CharField(
        max_length=150
    )

    criticality = models.CharField(
        max_length=20,
        choices=CRITICALITY_CHOICES,
        default="MEDIUM"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    confidentiality = models.PositiveSmallIntegerField(default=3)

    integrity = models.PositiveSmallIntegerField(default=3)

    availability = models.PositiveSmallIntegerField(default=3)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Actif"
        verbose_name_plural = "Actifs"

    def __str__(self):
        return f"{self.asset_code} - {self.name}"
class AssetAssignment(models.Model):

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name="assignments"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    assigned_at = models.DateTimeField(
        auto_now_add=True
    )

    returned_at = models.DateTimeField(
        blank=True,
        null=True
    )

    active = models.BooleanField(
        default=True
    )

    class Meta:
        ordering = ["-assigned_at"]
        verbose_name = "Affectation"
        verbose_name_plural = "Affectations"

    def __str__(self):
        return f"{self.asset.name} → {self.user.username}"
class AssetDocument(models.Model):

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    title = models.CharField(
        max_length=200
    )

    file = models.FileField(
        upload_to="assets/documents/"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title