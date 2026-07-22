from django.db import models
from django.contrib.auth.models import User

from assets.models import Asset


class AccessRequest(models.Model):

    ACCESS_LEVELS = [

        ("READ", "Lecture"),

        ("WRITE", "Lecture / Écriture"),

        ("ADMIN", "Administrateur"),

    ]

    STATUS = [

        ("PENDING", "En attente"),

        ("MANAGER_APPROVED", "Validée par le responsable"),

        ("MANAGER_REJECTED", "Refusée par le responsable"),

        ("RSSI_APPROVED", "Validée par le RSSI"),

        ("RSSI_REJECTED", "Refusée par le RSSI"),

        ("COMPLETED", "Terminée"),

        ("REVOKED", "Révoquée"),

    ]

    requester = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="access_requests"
    )

    asset = models.ForeignKey(
        Asset,
        on_delete=models.CASCADE,
        related_name="access_requests"
    )

    access_level = models.CharField(
        max_length=20,
        choices=ACCESS_LEVELS
    )

    justification = models.TextField()

    manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="manager_requests"
    )

    manager_comment = models.TextField(
        blank=True
    )

    manager_validation_date = models.DateTimeField(
        null=True,
        blank=True
    )

    rssi = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="rssi_requests"
    )

    rssi_comment = models.TextField(
        blank=True
    )

    rssi_validation_date = models.DateTimeField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS,
        default="PENDING"
    )

    start_date = models.DateField()

    end_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )
    class Meta:

      ordering = ["-created_at"]

      verbose_name = "Demande d'accès"

      verbose_name_plural = "Demandes d'accès"

      permissions = [

        ("approve_manager", "Peut valider une demande en tant que Responsable"),

        ("approve_rssi", "Peut valider une demande en tant que RSSI"),

        ("revoke_access", "Peut révoquer un accès"),
        ("approve_accessrequest", "Can approve access request"),
        ("reject_accessrequest", "Can reject access request"),
        ("revoke_accessrequest", "Can revoke access request"),
    ]
      def __str__(self):

        return f"{self.requester.username} → {self.asset.name}"