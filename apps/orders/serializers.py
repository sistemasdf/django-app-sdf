from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('order_id','spinningmills','weavers','invoice',
            'invoice_name','shipping_date','shipping_schedule','order_date',
            'order_status','order_enabled','created_at','updated_at')
