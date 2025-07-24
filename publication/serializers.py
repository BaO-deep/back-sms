# publication/serializers.py
from rest_framework import serializers
from .models import Theme, Publication, Souscription

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = '__all__'

class SouscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souscription
        fields = '__all__'
