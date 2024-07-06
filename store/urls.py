from django.urls import path
from .views import home, product_list, category_list, product_detail

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('categories/', category_list, name='category_list'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
]