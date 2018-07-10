from django.template.context_processors import request

from category.models import Category
from products.models import Products, ProductCategory

def menu(request):
    categories = Category.objects.filter(is_active=True).order_by('position')

    menu = dict()
    for category in categories:
        menu[category.named_id] = list()

    for pc in ProductCategory.objects.all():
        if pc.category_id.named_id in menu:
            menu[pc.category_id.named_id].append(pc.product_id.named_id)

    return {'menu': menu}


def bestsellers(request):
    bestsellers = Products.objects.filter(is_active=True, is_brand=True)

    return {'bestsellers': bestsellers}
