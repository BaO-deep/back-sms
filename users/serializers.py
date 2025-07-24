from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Role

User = get_user_model()

# Liste statique des permissions autorisées (directement ici si tu veux)
STATIC_PERMISSIONS = Role.STATIC_PERMISSIONS

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'permissions']

    def validate_permissions(self, value):
        invalid = [p for p in value if p not in STATIC_PERMISSIONS]
        if invalid:
            raise serializers.ValidationError(f"Invalid permissions: {invalid}")
        return value


class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True, read_only=True)
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'roles', 'permissions']
        read_only_fields = ['id']

    def get_permissions(self, obj):
        permissions = set()
        for role in obj.roles.all():
            permissions.update(role.permissions)
        return list(permissions)


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'roles']
        read_only_fields = ['id']

    def create(self, validated_data):
        roles = validated_data.pop('roles', [])
        user = User.objects.create_user(**validated_data)
        user.roles.set(roles)
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            if not User.objects.filter(email=email).exists():
                raise serializers.ValidationError("Email not found.")
        else:
            raise serializers.ValidationError('Must include "email" and "password".')

        return data


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Les mots de passe ne correspondent pas.")
        return data
