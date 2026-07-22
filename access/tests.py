from django.test import TestCase
from django.contrib.auth.models import User

from assets.models import AssetCategory, Asset
from .models import AccessRequest


class AccessRequestTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="ahmed",
            password="123456"
        )

        self.manager = User.objects.create_user(
            username="manager",
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
            manager=self.manager,
            start_date="2026-01-01",
            end_date="2026-12-31"
        )

    def test_request_created(self):

        self.assertEqual(
            self.request.status,
            "PENDING"
        )

    def test_manager(self):

        self.assertEqual(
            self.request.manager.username,
            "manager"
        )

    def test_asset(self):

        self.assertEqual(
            self.request.asset.name,
            "Serveur Linux"
        )

    def test_access_level(self):

        self.assertEqual(
            self.request.access_level,
            "READ"
        )