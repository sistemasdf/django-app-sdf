from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import password_validation, authenticate
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer,UserLoginSerializer
from .models import User
from apps.weavers.models import Weavers

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user, token = serializer.save()
            data = {
                'user': UserSerializer(user).data,
                'access_token': token
            }
            return Response(data, status=status.HTTP_200_OK)
        else:
            message_response = {"message": "El usuario no se encuentra registrado"}
            return Response(message_response, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='login-weavers')
    def loginweavers(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user, token = serializer.save()
            weavers_list = Weavers.objects.filter(weavers_document=request.data['username'],weavers_enabled=1).values('weavers_id','business_name','fiscal_address','delivery_address','weavers_name','weavers_lastname','weavers_email')
            if weavers_list.exists():
                print(weavers_list)
                data = {
                    'weavers_id': weavers_list[0]['weavers_id'],
                    'weavers_document': request.data['username'],
                    'business_name': weavers_list[0]['business_name'],
                    'fiscal_address': weavers_list[0]['fiscal_address'],
                    'delivery_address': weavers_list[0]['delivery_address'],
                    'weavers_name': weavers_list[0]['weavers_name'],
                    'weavers_lastname': weavers_list[0]['weavers_lastname'],
                    'weavers_email': weavers_list[0]['weavers_email'],
                    'access_token': token
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                message_response = {"message": "El Usuario no se encuentra registrado o se encuentra inactivo"}
                return Response(message_response, status=status.HTTP_200_OK)
        else:
            message_response = {"message": "El Nro. de Documento no se encuentra registrado"}
            return Response(message_response, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='login-backoffice')
    def loginbackoffice(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            serializer = UserLoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user, token = serializer.save()
            if UserSerializer(user).data['user_admin']==1:
                data = {
                    'first_name': UserSerializer(user).data['first_name'],
                    'last_name': UserSerializer(user).data['last_name'],
                    'access_token': token
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                message_response = {"message": "El Usuario no se encuentra registrado o se encuentra inactivo"}
                return Response(message_response, status=status.HTTP_200_OK)
        else:
            message_response = {"message": "El Usuario no se encuentra registrado"}
            return Response(message_response, status=status.HTTP_200_OK)
