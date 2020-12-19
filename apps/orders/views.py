from django.shortcuts import render
from rest_framework import viewsets, status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from apps.orders.serializers import OrderSerializer
from .models import Order, Weavers, SpinningMills
from apps.orderdetail.models import OrderDetail
from apps.yarntype.models import YarnType
from django.conf import settings
from datetime import datetime
from datetime import timedelta
import random
import pytz
import json

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

    @action(detail=False, methods=['get'], url_path='order-list')
    def orderlist(self, request):
        orderdate = self.request.query_params.get('order_date', None)
        if orderdate is not None:
            sorderdate = datetime(int(orderdate[:4]), int(orderdate[4:6]), int(orderdate[6:8]), 00, 00, 00, 000000, tzinfo=pytz.UTC)
            forderdate = datetime(int(orderdate[:4]), int(orderdate[4:6]), int(orderdate[6:8]), 23, 59, 59, 000000, tzinfo=pytz.UTC) + timedelta(days=1)
            queryset = Order.objects.filter(order_date__range=[sorderdate,forderdate],order_enabled=1).values("order_id","weavers__weavers_document","weavers__business_name","weavers__delivery_address","weavers__weavers_phone","weavers__weavers_email","invoice","invoice_name","shipping_date","shipping_schedule","order_date","order_status")
            for odata in queryset:
                odata['invoice'] = "https://sdfapiproject.herokuapp.com" + settings.MEDIA_URL + odata['invoice']
                odata['order_date'] = odata['order_date'].strftime('%Y-%m-%d %H:%M:%S')
                odata['shipping_date'] = odata['shipping_date'].strftime('%Y-%m-%d %H:%M:%S')
            data = json.dumps(list(queryset))
            return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)
        else:
            message_response = {"message": "No se enviaron filtros"}
            return Response(message_response, status=status.HTTP_200_OK)
