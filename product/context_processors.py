from .models import Product


def bestsellers(request):
    bestsellers = Product.objects.filter(is_active=True, is_brand=True)
    return {'bestsellers': bestsellers}

