# publication/serializers.py
from rest_framework import serializers
from .models import Theme, Publication, Souscription

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    theme = ThemeSerializer(read_only=True)  # détails complets du thème
    theme_id = serializers.PrimaryKeyRelatedField(
        queryset=Theme.objects.all(), source='theme', write_only=True
    )

    class Meta:
        model = Publication
        fields = [
            'id',
            'contenu',
            'date_publication',
            'actif',
            'theme',     # lecture
            'theme_id',  # écriture
            'date_creation'
        ]

class SouscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souscription
        fields = '__all__'
