from django.urls import path, include
from catalog.apps import CatalogConfig

# from catalog.views import home, contacts
from catalog.views import product_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    # path("", home, name="home"),
    # path("contacts/", contacts, name="contacts"),
    path('', product_list, name='product_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
]