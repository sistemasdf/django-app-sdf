from rest_framework import serializers
from .models import OrderDetail

class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ('orderdetail_id','order','yarntype','product_code',
            'number_bag','amount_kg','orderdetail_enabled',
            'created_at','updated_at')
