from django.urls import path, include
from catalog.apps import CatalogConfig

# from catalog.views import home, contacts
from catalog.views import ProductListView, ProductDetailView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    # path("", home, name="home"),
    # path("contacts/", contacts, name="contacts"),
    path('', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
]