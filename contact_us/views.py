from django.shortcuts import render


def contact_us_view(request):
    return render(request, 'contact_us_page.html')