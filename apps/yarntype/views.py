from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import YarnTypeSerializer
from .models import YarnType
import json

# Create your views here.
class YarnTypeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = YarnType.objects.all()
    serializer_class = YarnTypeSerializer

    @action(detail=False, methods=['get'], url_path='list-yarntype')
    def listyarntype(self, request):
        spinningmills_id = self.request.query_params.get('spinningmills_id', None)
        if spinningmills_id is not None:
            queryset = YarnType.objects.filter(spinningmills__spinningmills_id=spinningmills_id,yarntype_enabled=1).values("yarntype_id","spinningmills__spinningmills_id","yarntype_name","bag_volumen","kg_volumen")
            if queryset:
                data = json.dumps(list(queryset))
                return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)
            else:
                message_response = {"message": "La Empresa no cuenta con productos disponibles"}
                return Response(message_response, status=status.HTTP_200_OK)
        else:
            message_response = {"message": "No se enviaron datos a validar"}
            return Response(message_response, status=status.HTTP_200_OK)
