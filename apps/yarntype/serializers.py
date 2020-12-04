from rest_framework import serializers
from .models import YarnType

class YarnTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = YarnType
        fields = ('yarntype_id','spinningmills','yarntype_name','bag_volumen',
            'kg_volumen','yarntype_enabled','created_at','updated_at')
