from django.shortcuts import render, redirect
from .forms import AddressForm
from django.conf import settings

User = settings.AUTH_USER_MODEL

def address(request):
    form = AddressForm(request.POST or None)
    context = {
        "form":form,
    }
    # instance = form
    if form.is_valid():
        # instance.billing_profile = request.user.username
        form.save()
        context['form'] = AddressForm()
        return redirect("cart")

    return render(request,"carts/address.html",context) 