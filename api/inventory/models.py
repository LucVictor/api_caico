from django.db import models


class Inventory_Checked(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    checked_by = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)


class Item_Checked(models.Model):
    inventory_checked = models.ForeignKey(Inventory_Checked, related_name='items', on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_code = models.BigIntegerField()
    quantity_real = models.DecimalField(max_digits=10, decimal_places=3)
    quantity_system = models.DecimalField(max_digits=10, decimal_places=3)
    difference = models.DecimalField(max_digits=10, decimal_places=3)

