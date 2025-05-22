from django.db import models

class Type_Damaged(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

class Product_Damaged(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    type_of_damage = models.ForeignKey(Type_Damaged, on_delete=models.PROTECT, related_name='product_damaged')
    price = models.DecimalField(max_digits=10, decimal_places=3)
    created = models.DateField(auto_now_add=True)
    date = models.DateField()
    created_by = models.CharField(max_length=255)
