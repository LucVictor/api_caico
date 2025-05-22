from django.urls import path
from .views import get_products, create_product, delete_product, mod_product, get_product

urlpatterns = [
    path('/', get_products),
    path('/get/<int:pk>', get_product),
    path('/create/', create_product),
    path('/delete/<int:pk>', delete_product),
    path('/mod/<int:pk>', mod_product),
]
