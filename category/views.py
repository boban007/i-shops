from django.shortcuts import render
from category.models import Category
from product.models import Product, ProductCategory
from django.http import Http404

# Create your views here.
def index(request, category):
    category_name = category
    try:
        catalog = Category.objects.get(named_id=category)
    except Category.DoesNotExist:
        raise Http404

    products = ProductCategory.objects.filter(category_id=catalog)
    return render(request, 'category/index.html', locals())
