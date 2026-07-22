from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from access.models import AccessRequest
from assets.models import Asset
from audit.models import AuditLog
from habilitations.models import Permission


class Command(BaseCommand):
    help = "Ajoute des demandes, habilitations et journaux d'audit de démonstration."

    def handle(self, *args, **options):
        users = list(User.objects.filter(is_active=True).order_by("id")[:4])
        assets = list(Asset.objects.filter(status="ACTIVE").order_by("id")[:4])

        if len(users) < 2:
            raise CommandError("Créez au moins deux utilisateurs actifs avant de lancer cette commande.")
        if len(assets) < 2:
            raise CommandError("Créez au moins deux actifs actifs avant de lancer cette commande.")

        administrator = next((user for user in users if user.is_superuser), users[0])
        today = timezone.localdate()
        definitions = [
            (0, 0, "READ", "PENDING", "Consultation des procédures opérationnelles."),
            (1, 1, "WRITE", "MANAGER_APPROVED", "Mise à jour des informations de maintenance."),
            (0, 2 % len(assets), "READ", "RSSI_APPROVED", "Contrôle des équipements de sûreté."),
            (1, 0, "ADMIN", "MANAGER_REJECTED", "Administration temporaire demandée pour un test."),
            (0, 1, "WRITE", "COMPLETED", "Accès nécessaire au suivi quotidien des ressources."),
        ]

        requests = []
        for user_index, asset_index, level, status, justification in definitions:
            requester = users[user_index % len(users)]
            asset = assets[asset_index]
            request, created = AccessRequest.objects.get_or_create(
                requester=requester,
                asset=asset,
                justification=f"[DÉMO] {justification}",
                defaults={
                    "access_level": level,
                    "manager": administrator,
                    "rssi": administrator,
                    "status": status,
                    "start_date": today,
                    "end_date": today + timedelta(days=90),
                    "manager_comment": "Demande revue dans le cadre de la démonstration.",
                    "rssi_comment": "Validation de sécurité enregistrée.",
                },
            )
            if created:
                requests.append(request)

        approval_statuses = {"RSSI_APPROVED", "COMPLETED"}
        for request in AccessRequest.objects.filter(
            justification__startswith="[DÉMO]", status__in=approval_statuses
        ):
            Permission.objects.get_or_create(
                access_request=request,
                defaults={
                    "user": request.requester,
                    "asset": request.asset,
                    "access_level": request.access_level,
                    "granted_by": administrator,
                    "expiration_date": request.end_date,
                    "status": "ACTIVE",
                },
            )

        actions = [
            ("CREATE", "Access", "Création d'une demande d'accès de démonstration."),
            ("APPROVE", "Access", "Validation RSSI d'une demande de démonstration."),
            ("CREATE", "Habilitations", "Attribution automatique d'une habilitation."),
            ("UPDATE", "Assets", "Mise à jour d'un actif de démonstration."),
            ("LOGIN", "Accounts", "Connexion enregistrée pour la démonstration."),
            ("REJECT", "Access", "Refus managérial d'une demande de démonstration."),
        ]
        for index, (action, module, description) in enumerate(actions):
            AuditLog.objects.get_or_create(
                user=users[index % len(users)],
                action=action,
                module=module,
                description=f"[DÉMO] {description}",
            )

        self.stdout.write(self.style.SUCCESS(
            "Données ajoutées : demandes, habilitations et journaux d'audit de démonstration."
        ))
