from django.db import models

class Product_Shelflife(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    shelflife = models.DateField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    created_by = models.CharField(max_length=255)
