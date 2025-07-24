from django.core.management.base import BaseCommand
from users.models import Permission  # Assurez-vous que ce chemin d'importation est correct

class Command(BaseCommand):
    help = 'Import permissions directly from embedded JSON data'

    # Définition des données JSON directement dans la commande
    permissions_data = [
        {"code": "access-live-dashboard", "name": "Access Live Dashboard"},
        {"code": "create-articles", "name": "Create Articles"},
        {"code": "create-blacklist", "name": "Create Blacklist"},
        {"code": "create-broadcasts", "name": "Create Broadcasts"},
        {"code": "create-permissions", "name": "Create Permissions"},
        {"code": "create-roles", "name": "Create Roles"},
        {"code": "create-topics", "name": "Create Topics"},
        {"code": "create-users", "name": "Create Users"},
        {"code": "deactivate-customers", "name": "Deactivate Customers"},
        {"code": "deactivate-subscriptions", "name": "Deactivate Subscriptions"},
        {"code": "delete-articles", "name": "Delete Articles"},
        {"code": "delete-blacklist", "name": "Delete Blacklist"},
        {"code": "delete-broadcasts", "name": "Delete Broadcasts"},
        {"code": "delete-permissions", "name": "Delete Permissions"},
        {"code": "delete-roles", "name": "Delete Roles"},
        {"code": "delete-subscriptions", "name": "Delete Subscriptions"},
        {"code": "delete-topics", "name": "Delete Topics"},
        {"code": "delete-users", "name": "Delete Users"},
        {"code": "read-articles", "name": "Read Articles"},
        {"code": "read-billing", "name": "Read Billing"},
        {"code": "read-blacklist", "name": "Read Blacklist"},
        {"code": "read-broadcasts", "name": "Read Broadcasts"},
        {"code": "read-customers", "name": "Read Customers"},
        {"code": "read-dashboard", "name": "Read Dashboard"},
        {"code": "read-permissions", "name": "Read Permissions"},
        {"code": "read-roles", "name": "Read Roles"},
        {"code": "read-subscriptions", "name": "Read Subscriptions"},
        {"code": "read-topics", "name": "Read Topics"},
        {"code": "read-users", "name": "Read Users"},
        {"code": "update-articles", "name": "Update Articles"},
        {"code": "update-broadcasts", "name": "Update Broadcasts"},
        {"code": "update-permissions", "name": "Update Permissions"},
        {"code": "update-roles", "name": "Update Roles"},
        {"code": "update-topics", "name": "Update Topics"},
        {"code": "update-users", "name": "Update Users"}
    ]

    def handle(self, *args, **options):

        for perm_data in self.permissions_data:
            permission, created = Permission.objects.get_or_create(
                code=perm_data['code'],
                defaults={'name': perm_data['name']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created permission: {permission.code}'))
            else:
                self.stdout.write(self.style.WARNING(f'Permission already exists: {permission.code}'))

        self.stdout.write(self.style.SUCCESS('Permissions import completed'))
