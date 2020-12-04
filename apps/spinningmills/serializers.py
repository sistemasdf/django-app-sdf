from rest_framework import serializers
from .models import SpinningMills

class SpinningMillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SpinningMills
        fields = ('spinningmills_id','spinningmills_document','spinningmills_business_name','spinningmills_address',
            'spinningmills_name','spinningmills_lastname','spinningmills_phone','spinningmills_email',
            'spinningmills_enabled','created_at','updated_at')
