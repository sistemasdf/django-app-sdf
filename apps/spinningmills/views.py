from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import SpinningMillsSerializer
from .models import SpinningMills
import json

# Create your views here.
class SpinningMillsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SpinningMills.objects.all()
    serializer_class = SpinningMillsSerializer

    @action(detail=False, methods=['get'], url_path='validation')
    def validation(self, request):
        spinningmills_document = self.request.query_params.get('spinningmills_document', None)
        if spinningmills_document is not None:
            queryset = SpinningMills.objects.filter(spinningmills_document=spinningmills_document,spinningmills_enabled=1).values("spinningmills_id","spinningmills_document","spinningmills_business_name","spinningmills_address","spinningmills_email")
            if queryset:
                data = {
                    'spinningmills_id': queryset[0]['spinningmills_id'],
                    'spinningmills_document': queryset[0]['spinningmills_document'],
                    'spinningmills_business_name': queryset[0]['spinningmills_business_name'],
                    'spinningmills_address': queryset[0]['spinningmills_address'],
                    'spinningmills_email': queryset[0]['spinningmills_email']
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                message_response = {"message": "La Empresa vendedora no se encuentra registrada o se encuentra deshabilitada"}
                return Response(message_response, status=status.HTTP_200_OK)
        else:
            message_response = {"message": "No se enviaron datos a validar"}
            return Response(message_response, status=status.HTTP_200_OK)
