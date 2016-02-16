from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . models import Product


def index(request):
    # Fetch first 3 products in reverese alphabetical orderin
    product_list = Product.objects.order_by('-title')[:3]
    template = loader.get_template('webshop/index.html')
    context = {'product_list': product_list}
    return HttpResponse(template.render(context, request))


def detail(request, product_id):
    response = "The product id is %s."
    return HttpResponse(response % product_id)
