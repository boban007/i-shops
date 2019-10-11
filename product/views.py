from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage
from product.models import Product, ProductGeneric, Pack
from cart.forms import CartAddPackForm


def index(request, product):
    product_name = product
    try:
        product = Product.objects.get(named_id=product)
    except Product.DoesNotExist:
        raise Http404

    generic = list()
    try:
        query = ProductGeneric.objects.filter(product_id=product)
        for item in query:
            generic.append(str(item.generic_id))
    except ProductGeneric.DoesNotExist:
        pass

    try:
        pack = Pack.objects.filter(product_id=product)
    except Pack.DoesNotExists:
        raise Http404

    cart_pack_form = CartAddPackForm()

    return render(request, 'product/index.html', locals())


def all(request):
    all_product = Product.objects.all()
    try:
        page_num = request.GET['page']
    except KeyError:
        page_num = 1

    paginator = Paginator(all_product, 12)

    try:
        products = paginator.page(page_num)
    except InvalidPage:
        products = paginator.page(1)

    return render(request, 'product/all.html', locals())
