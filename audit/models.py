from django.db import models
from django.contrib.auth.models import User


class AuditLog(models.Model):

    ACTIONS = [

        ("LOGIN", "Connexion"),

        ("LOGOUT", "Déconnexion"),

        ("CREATE", "Création"),

        ("UPDATE", "Modification"),

        ("DELETE", "Suppression"),

        ("APPROVE", "Approbation"),

        ("REJECT", "Refus"),

        ("REVOKE", "Révocation"),

    ]

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    action = models.CharField(
        max_length=20,
        choices=ACTIONS
    )

    module = models.CharField(
        max_length=50
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-created_at"]

        verbose_name = "Journal d'audit"

        verbose_name_plural = "Journaux d'audit"

    def __str__(self):

        username = self.user.username if self.user else "Système"

        return f"{username} - {self.action}"