from django.test import TestCase
from django.contrib.auth.models import User

from assets.models import AssetCategory, Asset
from access.models import AccessRequest
from .models import Permission


class PermissionTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="ahmed",
            password="123456"
        )

        self.rssi = User.objects.create_user(
            username="rssi",
            password="123456"
        )

        self.category = AssetCategory.objects.create(
            name="Serveur"
        )

        self.asset = Asset.objects.create(
            asset_code="SRV001",
            name="Serveur Linux",
            category=self.category,
            owner=self.user,
            location="Datacenter",
            criticality="HIGH",
            status="ACTIVE",
            confidentiality=5,
            integrity=5,
            availability=5
        )

        self.request = AccessRequest.objects.create(
            requester=self.user,
            asset=self.asset,
            access_level="READ",
            justification="Maintenance",
            manager=self.rssi,
            start_date="2026-01-01",
            end_date="2026-12-31"
        )

        self.permission = Permission.objects.create(
            access_request=self.request,
            user=self.user,
            asset=self.asset,
            access_level="READ",
            granted_by=self.rssi,
            expiration_date="2026-12-31"
        )

    def test_permission_created(self):

        self.assertEqual(
            self.permission.status,
            "ACTIVE"
        )

    def test_permission_user(self):

        self.assertEqual(
            self.permission.user.username,
            "ahmed"
        )

    def test_permission_asset(self):

        self.assertEqual(
            self.permission.asset.name,
            "Serveur Linux"
        )

    def test_permission_level(self):

        self.assertEqual(
            self.permission.access_level,
            "READ"
        )