from django.shortcuts import render
from . import models


# Create your views here.

def header_component_view(request):
    return render(request, 'header_component.html')


def footer_component_view(request):
    return render(request, 'footer_component.html')


def index_view(request):
    return render(request, 'index.html')


def shop_page_view(request):
    products = models.Product.objects.all().order_by('-price')
    context = {
        'products': products
    }
    return render(request, 'shop_page.html', context=context)
