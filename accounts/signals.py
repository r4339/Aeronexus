from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):

    groups = [
        "Administrateur",
        "RSSI",
        "Responsable",
        "Employé",
        "Auditeur",
    ]

    for group in groups:
        Group.objects.get_or_create(name=group)