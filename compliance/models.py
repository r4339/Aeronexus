from django.db import models


class ComplianceCheck(models.Model):

    STATUS_CHOICES = [

        ("COMPLIANT", "Conforme"),

        ("NON_COMPLIANT", "Non conforme"),

        ("WARNING", "Avertissement"),

    ]

    name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    recommendation = models.TextField()

    checked_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        ordering = ["-checked_at"]

        verbose_name = "Contrôle de conformité"

        verbose_name_plural = "Contrôles de conformité"

    def __str__(self):

        return self.name