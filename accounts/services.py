from .models import UserProfile


class UserService:

    @staticmethod
    def get_all_users():
        return UserProfile.objects.select_related(
            "user",
            "department"
        )

    @staticmethod
    def get_user(profile_id):
        return UserProfile.objects.select_related(
            "user",
            "department"
        ).get(id=profile_id)

    @staticmethod
    def toggle_status(profile):
        profile.is_active_employee = not profile.is_active_employee
        profile.save()