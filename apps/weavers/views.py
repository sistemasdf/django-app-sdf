from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .serializers import WeaversSerializer
from .models import Weavers

# Create your views here.
class WeaversViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Weavers.objects.all()
    serializer_class = WeaversSerializer
