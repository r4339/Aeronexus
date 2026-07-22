from .models import AuditLog


class AuditService:

    @staticmethod
    def log(user, action, module, description):

        AuditLog.objects.create(

            user=user,

            action=action,

            module=module,

            description=description

        )

    @staticmethod
    def get_all_logs():

        return AuditLog.objects.all()

    @staticmethod
    def get_log(log_id):

        return AuditLog.objects.get(
            id=log_id
        )

    @staticmethod
    def logs_by_module(module):

        return AuditLog.objects.filter(
            module=module
        )

    @staticmethod
    def logs_by_action(action):

        return AuditLog.objects.filter(
            action=action
        )