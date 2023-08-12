from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms


def contact_us_view(request):
    # if request.method == 'POST':
    #     if request.POST['email'] == '':
    #         return render(request, 'contact_us_page.html', {'has_error': True})
    #     return redirect(reverse('index-page-url'))
    # elif request.method == 'GET':
    #     pass
    contact_us_form = forms.ContactUsForm()
    return render(request, 'contact_us_page.html', {'form': contact_us_form})
