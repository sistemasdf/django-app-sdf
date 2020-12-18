from django.shortcuts import render
from rest_framework import viewsets, status
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderDetailSerializer
from .models import OrderDetail
from apps.orders.models import Order
from apps.yarntype.models import YarnType
import datetime
import json

# Create your views here.
class OrderDetailViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer

    @action(detail=False, methods=['post'], url_path='order-update')
    def orderupdate(self, request):
        if request.data['order_id']:
            order = Order.objects.get(order_id=request.data['order_id'], order_enabled=1)
            if order:
                order.shipping_date = request.data['shipping_date']
                order.shipping_schedule = request.data['shipping_schedule']
                order.order_date = datetime.datetime.now()
                order.save()
                for element in request.data['order_detail']:
                    yarntype = YarnType.objects.get(yarntype_id=element['yarntype_id'], yarntype_enabled=1)
                    orderdetail = OrderDetail()
                    orderdetail.order = order
                    orderdetail.yarntype = yarntype
                    orderdetail.product_code = element['product_code']
                    orderdetail.number_bag = element['number_bag']
                    orderdetail.amount_kg = element['amount_kg']
                    orderdetail.save()
                dataorder = Order.objects.filter(order_id=request.data['order_id'], order_enabled=1).values("order_id","order_date","shipping_date","shipping_schedule")
                data = {
                    'order_id': dataorder[0]['order_id'],
                    'order_date': dataorder[0]['order_date'],
                    'shipping_date': dataorder[0]['shipping_date'],
                    'shipping_schedule': dataorder[0]['shipping_schedule']
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                message_response = {"message": "La orden no existe"}
                return Response(message_response, status=status.HTTP_200_OK)
        else:
            message_response = {"message": "No se enviaron los datos correctos"}
            return Response(message_response, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='order-detail')
    def orderdetail(self, request):
        orderid = self.request.query_params.get('order_id', None)
        if orderid:
            orderdetail = OrderDetail.objects.filter(order__order_id=orderid, orderdetail_enabled=1).values('orderdetail_id','yarntype__yarntype_name','product_code','number_bag','amount_kg')
            if orderdetail:
                data = json.dumps(list(orderdetail))
                return HttpResponse(data, content_type='application/json', status=status.HTTP_200_OK)
            else:
                message_response = {"message": "La orden no cuenta con detalle"}
                return Response(message_response, status=status.HTTP_200_OK)
        else:
            message_response = {"message": "No se enviaron los datos correctos"}
            return Response(message_response, status=status.HTTP_200_OK)
