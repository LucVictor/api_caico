from django.urls import path
from .views import get_product, create_product

urlpatterns = [
    path('/<int:pk>', get_product),
    path('/create/', create_product),

]