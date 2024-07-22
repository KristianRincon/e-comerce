from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, CartItem, Cart
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product':product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'{product.name} ha sido agregado al carrito')
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all() # type: ignore
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    return render(request, 'cart_detail.html', {'cart': cart, 'cart_items': cart_items})

