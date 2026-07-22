from django.test import TestCase

from .models import ComplianceCheck


class ComplianceCheckTest(TestCase):

    def setUp(self):

        self.check = ComplianceCheck.objects.create(

            name="Comptes inactifs",

            description="Vérification des comptes utilisateurs inactifs.",

            status="WARNING",

            recommendation="Désactiver les comptes inutilisés."

        )

    def test_check_created(self):

        self.assertEqual(

            self.check.name,

            "Comptes inactifs"

        )

    def test_status(self):

        self.assertEqual(

            self.check.status,

            "WARNING"

        )

    def test_recommendation(self):

        self.assertEqual(

            self.check.recommendation,

            "Désactiver les comptes inutilisés."

        )