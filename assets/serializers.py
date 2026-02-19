from rest_framework import serializers
from .models import AssetMaster

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetMaster
        fields = ['AssetTagID', 'AssetSerialNo']
