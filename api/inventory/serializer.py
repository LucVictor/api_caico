from rest_framework import serializers
from .models import Inventory_Checked, Item_Checked

class Inventory_CheckedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory_Checked
        fields = '__all__'

class Item_CheckedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Checked
        fields = '__all__'