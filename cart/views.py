from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from product.models import Pack
from .cart import Cart
from .forms import CartAddPackForm


@require_POST
def add(request, pack_id):
    cart = Cart(request)
    pack = get_object_or_404(Pack, id=pack_id)
    form = CartAddPackForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(pack=pack, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:detail')


def remove(request, pack_id):
    cart = Cart(request)
    pack = get_object_or_404(Pack, id=pack_id)
    cart.remove(pack)
    return redirect('cart:detail')


def adjust(request, pack_id, change):
    cart = Cart(request)
    pack = get_object_or_404(Pack, id=pack_id)
    quantity = 1
    if change == '-':
        quantity = -1
    cart.adjust(pack=pack, quantity=quantity)
    return redirect('cart:detail')


def detail(request):
    cart = Cart(request)
    if cart:
        return render(request, 'cart/detail.html', locals())
    else:
        return render(request, 'cart/empty.html')


def checkout(request):
    cart = Cart(request)
    if cart:
        return render(request, 'cart/checkout.html', {'cart': cart})
    else:
        return render(request, 'cart/empty.html')

