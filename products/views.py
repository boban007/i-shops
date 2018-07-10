from django.shortcuts import render
from django.http import Http404
from products.models import Products


def index(request, product):
    product_name = product
    try:
        product = Products.objects.get(named_id=product)
    except Products.DoesNotExist:
        raise Http404

    return render(request, 'products/index.html', locals())
