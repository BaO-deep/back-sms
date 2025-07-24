from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Rôles', {'fields': ('roles',)}),
    )
    filter_horizontal = ('roles', 'groups')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Role, RoleAdmin)