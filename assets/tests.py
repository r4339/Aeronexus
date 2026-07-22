from django.test import TestCase
from django.contrib.auth.models import User

from .models import (
    AssetCategory,
    Asset,
    AssetAssignment,
)


class AssetModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="admin",
            password="admin123"
        )

        self.category = AssetCategory.objects.create(
            name="Serveur"
        )

        self.asset = Asset.objects.create(
            asset_code="SRV001",
            name="Serveur Production",
            category=self.category,
            owner=self.user,
            location="Datacenter",
            criticality="HIGH",
            status="ACTIVE",
            confidentiality=5,
            integrity=5,
            availability=5
        )


    def test_asset_created(self):

        self.assertEqual(
            self.asset.name,
            "Serveur Production"
        )


    def test_asset_category(self):

        self.assertEqual(
            self.asset.category.name,
            "Serveur"
        )


    def test_asset_status(self):

        self.assertEqual(
            self.asset.status,
            "ACTIVE"
        )


class AssignmentTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="user1",
            password="123456"
        )

        self.category = AssetCategory.objects.create(
            name="Firewall"
        )

        self.asset = Asset.objects.create(
            asset_code="FW001",
            name="Firewall Fortinet",
            category=self.category,
            owner=self.user,
            location="Salle Réseau",
            criticality="CRITICAL",
            status="ACTIVE",
            confidentiality=5,
            integrity=5,
            availability=5
        )

        self.assignment = AssetAssignment.objects.create(
            asset=self.asset,
            user=self.user
        )


    def test_assignment_created(self):

        self.assertTrue(
            self.assignment.active
        )


    def test_return_asset(self):

        self.assignment.active = False

        self.assignment.save()

        self.assertFalse(
            self.assignment.active
        )