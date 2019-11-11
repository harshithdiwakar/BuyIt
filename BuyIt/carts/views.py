from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Cart
from products.models import Product

def cart_view(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
    
    if the_id:
        cart = Cart.objects.get(id = the_id)
        context = {
            "cart":cart
        }
    else:
        empty_message = "Cart is Empty!"
        context = {
            "empty": True,
            "empty_message": empty_message
        }

    return render(request,"carts/cart.html",context)


def update_cart(request,slug):
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id

    cart = Cart.objects.get(id = the_id)

    try:
        item = Product.objects.get(slug = slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    if not item in cart.products.all():
        cart.products.add(item)
    else:
        cart.products.remove(item)

    cart_total = 0.00
    for item in cart.products.all():
        cart_total += float(item.price)
    
    request.session['total_items'] = cart.products.count()
    cart.total = (1.15 * cart_total)
    cart.save()


    return redirect(reverse("cart"))