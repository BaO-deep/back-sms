from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField  # PostgreSQL uniquement

class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)
    permissions = ArrayField(
        models.CharField(max_length=100),
        blank=True,
        default=list
    )

    # Liste complète des permissions autorisées dans l’app
    STATIC_PERMISSIONS = [
        "access-live-dashboard",
        "create-articles",
        "create-blacklist",
        "create-broadcasts",
        "create-permissions",
        "create-roles",
        "create-topics",
        "create-users",
        "deactivate-customers",
        "deactivate-subscriptions",
        "delete-articles",
        "delete-blacklist",
        "delete-broadcasts",
        "delete-permissions",
        "delete-roles",
        "delete-subscriptions",
        "delete-topics",
        "delete-users",
        "read-articles",
        "read-billing",
        "read-blacklist",
        "read-broadcasts",
        "read-customers",
        "read-dashboard",
        "read-permissions",
        "read-roles",
        "read-subscriptions",
        "read-topics",
        "read-users",
        "update-articles",
        "update-broadcasts",
        "update-permissions",
        "update-roles",
        "update-topics",
        "update-users",
    ]

    def __str__(self):
        return self.name

class User(AbstractUser):
    email = models.EmailField(unique=True)
    roles = models.ManyToManyField(Role, related_name="users")

    def __str__(self):
        return self.username

    def get_all_permissions(self):
        all_perms = set()
        for role in self.roles.all():
            all_perms.update(role.permissions)
        return list(all_perms)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
