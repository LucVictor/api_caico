
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products', include('products.urls')),
    path('api/shelflife', include('shelflife.urls')),
    path('api/damaged', include('damaged.urls')),
    path('api/checked', include('inventory.urls')),
]
