from django.test import TestCase
from django.contrib.auth.models import User

from .models import Department, UserProfile


class UserProfileTest(TestCase):

    def setUp(self):

        self.department = Department.objects.create(
            name="Informatique"
        )

        self.user = User.objects.create_user(
            username="admin",
            first_name="Ahmed",
            last_name="Bennani",
            email="admin@test.com",
            password="admin123"
        )

        self.profile = UserProfile.objects.create(
            user=self.user,
            matricule="EMP001",
            phone="0600000000",
            department=self.department,
            job_title="Administrateur Système",
            is_active_employee=True
        )

    def test_profile_created(self):

        self.assertEqual(
            self.profile.user.username,
            "admin"
        )

    def test_department(self):

        self.assertEqual(
            self.profile.department.name,
            "Informatique"
        )

    def test_job_title(self):

        self.assertEqual(
            self.profile.job_title,
            "Administrateur Système"
        )

    def test_employee_status(self):

        self.assertTrue(
            self.profile.is_active_employee
        )

    def test_matricule(self):

        self.assertEqual(
            self.profile.matricule,
            "EMP001"
        )