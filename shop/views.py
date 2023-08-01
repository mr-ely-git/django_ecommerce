from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, 'index.html')


def header_component_view(request):
    return render(request, 'header_component.html')


def footer_component_view(request):
    return render(request, 'footer_component.html')