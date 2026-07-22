from django.db import models
from django.contrib.auth.models import User

from assets.models import Asset
from access.models import AccessRequest


class Permission(models.Model):

    STATUS_CHOICES = [

        ("ACTIVE", "Active"),

        ("EXPIRED", "Expirée"),

        ("REVOKED", "Révoquée"),

    ]

    access_request = models.OneToOneField(
        AccessRequest,
        on_delete=models.CASCADE,
        related_name="permission"
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="permissions"
    )

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name="permissions"
    )

    access_level = models.CharField(
        max_length=20
    )

    granted_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="granted_permissions"
    )

    granted_at = models.DateTimeField(
        auto_now_add=True
    )

    expiration_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    revoked_at = models.DateTimeField(
        null=True,
        blank=True
    )

    revoke_reason = models.TextField(
        blank=True
    )
class Meta:

    ordering = ["-granted_at"]

    verbose_name = "Habilitation"

    verbose_name_plural = "Habilitations"

    permissions = [

        (
            "revoke_permission",
            "Peut révoquer une habilitation"
        ),

    ]
    def __str__(self):

        return f"{self.user.username} - {self.asset.name}"