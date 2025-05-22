from rest_framework import serializers
from .models import Product_Damaged

class Product_DamagedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Damaged
        fields = '__all__'