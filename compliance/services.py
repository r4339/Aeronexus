from .models import ComplianceCheck


class ComplianceService:

    @staticmethod
    def get_all_checks():

        return ComplianceCheck.objects.all()


    @staticmethod
    def get_check(check_id):

        return ComplianceCheck.objects.get(
            id=check_id
        )


    @staticmethod
    def compliant_checks():

        return ComplianceCheck.objects.filter(
            status="COMPLIANT"
        )


    @staticmethod
    def warning_checks():

        return ComplianceCheck.objects.filter(
            status="WARNING"
        )


    @staticmethod
    def non_compliant_checks():

        return ComplianceCheck.objects.filter(
            status="NON_COMPLIANT"
        )