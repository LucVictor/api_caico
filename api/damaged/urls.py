from django.urls import path
from .views import get_products, create_product, delete_product, mod_product

urlpatterns = [
    path('', get_products),
    path('create/', create_product),
    path('delete/<int:pk>', delete_product),
    path('mod/<int:pk>', mod_product),
]