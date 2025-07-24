# publication/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Theme
    path('themes/', views.ThemeListCreateAPIView.as_view(), name='theme-list-create'),
    path('themes/<int:pk>/', views.ThemeDetailAPIView.as_view(), name='theme-detail'),
    # Publication
    path('publications/', views.PublicationListCreateAPIView.as_view(), name='publication-list-create'),
    path('publications/<int:pk>/', views.PublicationDetailAPIView.as_view(), name='publication-detail'),
    # Souscription
    path('souscriptions/', views.SouscriptionListCreateAPIView.as_view(), name='souscription-list-create'),
    path('souscriptions/<int:pk>/', views.SouscriptionDetailAPIView.as_view(), name='souscription-detail'),
]
