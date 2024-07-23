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

@login_required
def remove_from_cart(request, product_id):
    # Obtener el producto por su ID, si no existe devuelve un 404
    product = get_object_or_404(Product, id=product_id)
    # Obtener el carrito del usuario. No es necesario verificar si se crea un nuevo carrito porque estamos removiendo productos
    cart = Cart.objects.get(user=request.user)

    try:
        # Obtener el CartItem correspondiente al carrito y producto
        cart_item = CartItem.objects.get(cart=cart, product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
        messages.success(request, f'{product.name} ha sido eliminado del carrito')
    except CartItem.DoesNotExist:
        messages.error(request, f'{product.name} no se encuentra en el carrito')

    return redirect('cart_detail')