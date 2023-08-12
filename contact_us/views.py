from django.shortcuts import render, redirect
from django.urls import reverse


def contact_us_view(request):
    if request.method == 'POST':
        if request.POST['email'] == '':
            return render(request, 'contact_us_page.html', {'has_error': True})
        return redirect(reverse('index-page-url'))
    elif request.method == 'GET':
        pass
    return render(request, 'contact_us_page.html')
