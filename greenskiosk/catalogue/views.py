from django.shortcuts import render

# Create your views here.
from catalogue.models import Product


def products_list(request):
    products= Product.objects.all()
    return render(request, 'products_list.html', {'products': products})