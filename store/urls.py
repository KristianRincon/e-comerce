from django.urls import path
from .views import home, product_list, category_list, product_detail, add_to_cart, cart_detail

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('categories/', category_list, name='category_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
]