from rest_framework import serializers
from .models import Weavers

class WeaversSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weavers
        fields = ('weavers_id','weavers_document','business_name','fiscal_address',
            'delivery_address','weavers_name','weavers_lastname','weavers_phone',
            'weavers_email','created_at','updated_at')
