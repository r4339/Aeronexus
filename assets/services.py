from .models import (
    Asset,
    AssetAssignment,
)


class AssetService:

    @staticmethod
    def get_all_assets():
        """
        Retourne tous les actifs.
        """
        return Asset.objects.all()


    @staticmethod
    def get_asset_by_id(asset_id):
        """
        Retourne un actif à partir de son ID.
        """
        return Asset.objects.get(id=asset_id)


    @staticmethod
    def create_asset(form):
        """
        Enregistre un nouvel actif.
        """
        return form.save()


    @staticmethod
    def update_asset(form):
        """
        Met à jour un actif.
        """
        return form.save()


    @staticmethod
    def delete_asset(asset):
        """
        Supprime un actif.
        """
        asset.delete()


    @staticmethod
    def get_active_assets():
        """
        Retourne les actifs actifs.
        """
        return Asset.objects.filter(status="ACTIVE")


    @staticmethod
    def get_critical_assets():
        """
        Retourne les actifs critiques.
        """
        return Asset.objects.filter(
            criticality="CRITICAL"
        )


    @staticmethod
    def get_assets_in_maintenance():
        """
        Retourne les actifs en maintenance.
        """
        return Asset.objects.filter(
            status="MAINTENANCE"
        )


class AssetAssignmentService:

    @staticmethod
    def assign_asset(form):
        """
        Affecte un actif à un utilisateur.
        """
        return form.save()


    @staticmethod
    def get_all_assignments():
        """
        Retourne toutes les affectations.
        """
        return AssetAssignment.objects.all()


    @staticmethod
    def get_assignment_by_id(assignment_id):
        """
        Retourne une affectation.
        """
        return AssetAssignment.objects.get(
            id=assignment_id
        )


    @staticmethod
    def return_asset(assignment):

        assignment.active = False

        assignment.save()

        return assignment