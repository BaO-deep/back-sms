from django.urls import path
from .views import UserViewSet, RoleViewSet  # 👈 SUPPRIME PermissionViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # User URLs
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='user-detail'),
    path('login/', UserViewSet.as_view({'post': 'login'}), name='user-login'),
    path('change-password/', UserViewSet.as_view({'post': 'change_password'}), name='user-change-password'),
    path('profile/', UserViewSet.as_view({'get': 'profile', 'put': 'profile', 'patch': 'profile'}), name='user-profile'),

    # Role URLs
    path('roles/', RoleViewSet.as_view({'get': 'list', 'post': 'create'}), name='role-list'),
    path('roles/<int:pk>/', RoleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='role-detail'),

    # JWT URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
