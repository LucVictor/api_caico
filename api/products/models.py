from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.IntegerField()
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3)

