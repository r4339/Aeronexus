from django.utils import timezone

from .models import Permission


class PermissionService:

    @staticmethod
    def get_all_permissions():

        return Permission.objects.all()


    @staticmethod
    def get_permission(permission_id):

        return Permission.objects.get(
            id=permission_id
        )


    @staticmethod
    def revoke(permission, reason):

        permission.status = "REVOKED"

        permission.revoked_at = timezone.now()

        permission.revoke_reason = reason

        permission.save()


    @staticmethod
    def expire(permission):

        permission.status = "EXPIRED"

        permission.save()


    @staticmethod
    def active_permissions():

        return Permission.objects.filter(
            status="ACTIVE"
        )


    @staticmethod
    def expired_permissions():

        return Permission.objects.filter(
            status="EXPIRED"
        )


    @staticmethod
    def revoked_permissions():

        return Permission.objects.filter(
            status="REVOKED"
        )