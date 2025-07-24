# publication/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Theme, Publication, Souscription
from .serializers import ThemeSerializer, PublicationSerializer, SouscriptionSerializer
from django.shortcuts import get_object_or_404

# --- THEME ---
class ThemeListCreateAPIView(APIView):
    def get(self, request):
        themes = Theme.objects.all()
        serializer = ThemeSerializer(themes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ThemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ThemeDetailAPIView(APIView):
    def get(self, request, pk):
        theme = get_object_or_404(Theme, pk=pk)
        serializer = ThemeSerializer(theme)
        return Response(serializer.data)

    def put(self, request, pk):
        theme = get_object_or_404(Theme, pk=pk)
        serializer = ThemeSerializer(theme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        theme = get_object_or_404(Theme, pk=pk)
        theme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- PUBLICATION ---
class PublicationListCreateAPIView(APIView):
    def get(self, request):
        publications = Publication.objects.all()
        serializer = PublicationSerializer(publications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PublicationDetailAPIView(APIView):
    def get(self, request, pk):
        publication = get_object_or_404(Publication, pk=pk)
        serializer = PublicationSerializer(publication)
        return Response(serializer.data)

    def put(self, request, pk):
        publication = get_object_or_404(Publication, pk=pk)
        serializer = PublicationSerializer(publication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        publication = get_object_or_404(Publication, pk=pk)
        publication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# --- SOUSCRIPTION ---
class SouscriptionListCreateAPIView(APIView):
    def get(self, request):
        souscriptions = Souscription.objects.all()
        serializer = SouscriptionSerializer(souscriptions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SouscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SouscriptionDetailAPIView(APIView):
    def get(self, request, pk):
        souscription = get_object_or_404(Souscription, pk=pk)
        serializer = SouscriptionSerializer(souscription)
        return Response(serializer.data)

    def put(self, request, pk):
        souscription = get_object_or_404(Souscription, pk=pk)
        serializer = SouscriptionSerializer(souscription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        souscription = get_object_or_404(Souscription, pk=pk)
        souscription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
