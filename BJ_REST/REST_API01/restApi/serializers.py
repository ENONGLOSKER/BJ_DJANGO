from rest_framework import serializers
from .models import produkModel

class produkSerializer(serializers.ModelSerializer):
    class Meta:
        model  = produkModel
        fields = "__all__"