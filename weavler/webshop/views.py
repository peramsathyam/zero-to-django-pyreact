from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Product


def index(request):
    # Fetch first 3 products in reverese alphabetical orderin
    product_list = Product.objects.order_by('-title')[:3]
    context = {'product_list': product_list}
    return render(request, 'webshop/index.html', context)


def detail(request, product_id):
    response = "The product id is %s."
    return HttpResponse(response % product_id)
