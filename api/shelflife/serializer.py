from rest_framework import serializers
from .models import Product_Shelflife

class Product_ShelflifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Shelflife
        fields = '__all__'