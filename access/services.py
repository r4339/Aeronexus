from django.utils import timezone
from .models import AccessRequest


class AccessRequestService:

    # =====================================================
    # LISTES
    # =====================================================

    @staticmethod
    def get_all_requests():

        return (
            AccessRequest.objects
            .select_related(
                "requester",
                "asset",
                "manager",
                "rssi"
            )
            .order_by("-created_at")
        )


    @staticmethod
    def get_request(request_id):

        return (
            AccessRequest.objects
            .select_related(
                "requester",
                "asset",
                "manager",
                "rssi"
            )
            .get(pk=request_id)
        )


    # =====================================================
    # CREATION
    # =====================================================

    @staticmethod
    def create_request(form, user):

        access_request = form.save(commit=False)

        access_request.requester = user

        access_request.status = "PENDING"

        access_request.created_at = timezone.now()

        access_request.save()

        return access_request


    # =====================================================
    # MODIFICATION
    # =====================================================

    @staticmethod
    def update_request(form):

        access_request = form.save()

        return access_request


    # =====================================================
    # SUPPRESSION
    # =====================================================

    @staticmethod
    def delete_request(access_request):

        access_request.delete()


    # =====================================================
    # DEMANDES EN ATTENTE
    # =====================================================

    @staticmethod
    def pending_requests():

        return AccessRequest.objects.filter(
            status="PENDING"
        ).order_by("-created_at")
        # =====================================================
    # VALIDATION PAR LE RESPONSABLE
    # =====================================================

    @staticmethod
    def manager_approve(access_request, manager):

        access_request.manager = manager

        access_request.manager_validation_date = timezone.now()

        access_request.status = "MANAGER_APPROVED"

        access_request.save()

        return access_request


    @staticmethod
    def manager_reject(access_request, manager, comment):

        access_request.manager = manager

        access_request.manager_comment = comment

        access_request.manager_validation_date = timezone.now()

        access_request.status = "MANAGER_REJECTED"

        access_request.save()

        return access_request


    # =====================================================
    # VALIDATION PAR LE RSSI
    # =====================================================

    @staticmethod
    def rssi_approve(access_request, rssi):

        access_request.rssi = rssi

        access_request.rssi_validation_date = timezone.now()

        access_request.status = "RSSI_APPROVED"

        access_request.save()

        return access_request


    @staticmethod
    def rssi_reject(access_request, rssi, comment):

        access_request.rssi = rssi

        access_request.rssi_comment = comment

        access_request.rssi_validation_date = timezone.now()

        access_request.status = "RSSI_REJECTED"

        access_request.save()

        return access_request


    # =====================================================
    # REVOCATION
    # =====================================================

    @staticmethod
    def revoke(access_request):

        access_request.status = "REVOKED"

        access_request.revoked_at = timezone.now()

        access_request.save()

        return access_request
        # =====================================================
    # LISTES PAR ETAT
    # =====================================================

    @staticmethod
    def approved_requests():

        return (
            AccessRequest.objects
            .filter(
                status__in=[
                    "RSSI_APPROVED",
                    "COMPLETED"
                ]
            )
            .select_related(
                "requester",
                "asset",
                "manager",
                "rssi"
            )
            .order_by("-created_at")
        )


    @staticmethod
    def rejected_requests():

        return (
            AccessRequest.objects
            .filter(
                status__in=[
                    "MANAGER_REJECTED",
                    "RSSI_REJECTED"
                ]
            )
            .select_related(
                "requester",
                "asset",
                "manager",
                "rssi"
            )
            .order_by("-created_at")
        )


    # =====================================================
    # STATISTIQUES
    # =====================================================

    @staticmethod
    def total_requests():

        return AccessRequest.objects.count()


    @staticmethod
    def pending_count():

        return AccessRequest.objects.filter(
            status="PENDING"
        ).count()


    @staticmethod
    def approved_count():

        return AccessRequest.objects.filter(
            status__in=[
                "RSSI_APPROVED",
                "COMPLETED"
            ]
        ).count()


    @staticmethod
    def rejected_count():

        return AccessRequest.objects.filter(
            status__in=[
                "MANAGER_REJECTED",
                "RSSI_REJECTED"
            ]
        ).count()


    @staticmethod
    def latest_requests(limit=5):

        return (
            AccessRequest.objects
            .select_related(
                "requester",
                "asset"
            )
            .order_by("-created_at")[:limit]
        )