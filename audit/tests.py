from django.test import TestCase
from django.contrib.auth.models import User

from .models import AuditLog


class AuditLogTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="admin",
            password="123456"
        )

        self.log = AuditLog.objects.create(
            user=self.user,
            action="CREATE",
            module="Accounts",
            description="Création d'un utilisateur."
        )

    def test_log_created(self):

        self.assertEqual(
            self.log.action,
            "CREATE"
        )

    def test_log_module(self):

        self.assertEqual(
            self.log.module,
            "Accounts"
        )

    def test_log_user(self):

        self.assertEqual(
            self.log.user.username,
            "admin"
        )

    def test_log_description(self):

        self.assertEqual(
            self.log.description,
            "Création d'un utilisateur."
        )