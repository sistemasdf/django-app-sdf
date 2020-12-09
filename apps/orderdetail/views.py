from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderDetailSerializer
from .models import OrderDetail

# Create your views here.
class OrderDetailViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
