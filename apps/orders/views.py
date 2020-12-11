from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from apps.orders.serializers import OrderSerializer
from .models import Order, Weavers, SpinningMills
from apps.orderdetail.models import OrderDetail
from apps.yarntype.models import YarnType
import random

# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        print (request.FILES['invoice'])
        print (request.data['weavers_id'])
        print (request.data['spinningmills_id'])
        file_name = request.FILES['invoice'].name
        extension = file_name.split(".")
        orderid = 0;
        while True:
            request.FILES['invoice'].name = '{0}{1}{2}{3}{4}.{5}'.format("invoice",random.choice("AEIOU"),random.choice("AEIOU"),random.randrange(1000),random.randrange(1000),extension[len(extension)-1])
            #pruebaname = '{0}{1}{2}{3}{4}.{5}'.format("invoice",random.choice("AEIOU"),random.choice("AEIOU"),random.randrange(1000),random.randrange(1000),".pdf")
            order_list = Order.objects.filter(invoice_name=request.FILES['invoice'].name).values("order_id")
            if not order_list:
                weavers = Weavers.objects.get(weavers_id=request.data['weavers_id'])
                spinningmills = SpinningMills.objects.get(spinningmills_id=request.data['spinningmills_id'])
                order = Order()
                order.weavers = weavers
                order.spinningmills = spinningmills
                order.invoice = request.FILES['invoice']
                order.invoice_name = request.FILES['invoice'].name
                #order.invoice_name = pruebaname
                order.save()
                orderid = order.order_id
                break
        message_response = {
            "success": "Se guardo correctamente",
            "order_id": orderid
        }
        return Response(message_response, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'], url_path='order-test')
    def ordertest(self, request):
        #print (request.FILES['invoice'])
        print (request.data['weavers_id'])
        print (request.data['spinningmills_id'])
        #file_name = request.FILES['invoice'].name
        #extension = file_name.split(".")
        orderid = 0;
        while True:
            #request.FILES['invoice'].name = '{0}{1}{2}{3}{4}.{5}'.format("invoice",random.choice("AEIOU"),random.choice("AEIOU"),random.randrange(1000),random.randrange(1000),extension[len(extension)-1])
            pruebaname = '{0}{1}{2}{3}{4}.{5}'.format("invoice",random.choice("AEIOU"),random.choice("AEIOU"),random.randrange(1000),random.randrange(1000),".pdf")
            order_list = Order.objects.filter(invoice_name=pruebaname).values("order_id")
            if not order_list:
                weavers = Weavers.objects.get(weavers_id=request.data['weavers_id'])
                spinningmills = SpinningMills.objects.get(spinningmills_id=request.data['spinningmills_id'])
                order = Order()
                order.weavers = weavers
                order.spinningmills = spinningmills
                #order.invoice = request.FILES['invoice']
                #order.invoice_name = request.FILES['invoice'].name
                order.invoice_name = pruebaname
                order.save()
                orderid = order.order_id
                break
        message_response = {
            "success": "Se guardo correctamente",
            "order_id": orderid
        }
        return Response(message_response, status=status.HTTP_201_CREATED)
