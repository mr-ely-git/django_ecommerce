from django.shortcuts import render
from . import models


# Create your views here.

def header_component_view(request):
    return render(request, 'header_component.html')


def footer_component_view(request):
    return render(request, 'footer_component.html')


def index_page_view(request):
    return render(request, 'index_page.html')


def shop_page_view(request):
    products = models.Product.objects.all().order_by('-price')
    context = {
        'products': products
    }
    return render(request, 'shop_page.html', context=context)


def single_page_view(request, slug):
    context = {
        'product': models.Product.objects.get(slug=slug)
    }
    return render(request, 'single_product_page.html', context=context)
