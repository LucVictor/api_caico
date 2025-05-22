from django.urls import path
from .views import get_inventory, mod_inventory, delete_inventory, create_invetory, get_items, delete_item, create_item

urlpatterns = [
    path('inventorycheck', get_inventory),
    path('inventorycheck/create/', create_invetory),
    path('inventorycheck/delete/<int:pk>', delete_inventory),
    path('inventorycheck/mod/<int:pk>', mod_inventory),
    path('items_check', get_items),
    path('items_check/create/', create_item),
    path('items_check/delete/<int:pk>', delete_item),
]