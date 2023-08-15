from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from . import forms
from . import models


class ContactUsView(View):
    def get(self, request):
        contact_us_form = forms.ContactUsModelForm()
        return render(request, 'contact_us_page.html', {'form': contact_us_form})

    def post(self, request):
        contact_us_form = forms.ContactUsModelForm(request.POST)
        if contact_us_form.is_valid():
            contact_us_form.save()
            return redirect(reverse('index-page-url'))
        return render(request, 'contact_us_page.html', {'form': contact_us_form})


def contact_us_view(request):
    # if request.method == 'POST':
    #     if request.POST['email'] == '':
    #         return render(request, 'contact_us_page.html', {'has_error': True})
    #     return redirect(reverse('index-page-url'))
    # elif request.method == 'GET':
    #     pass
    if request.method == 'POST':
        # contact_us_form = forms.ContactUsForm(request.POST)
        contact_us_form = forms.ContactUsModelForm(request.POST)
        if contact_us_form.is_valid():
            # contact_model = models.ContactUsForm(
            #     email=contact_us_form.cleaned_data.get('email'),
            #     subject=contact_us_form.cleaned_data.get('subject'),
            #     message=contact_us_form.cleaned_data.get('message'),
            # )
            # contact_model.save()
            contact_us_form.save()
            return redirect(reverse('index-page-url'))

    else:
        # contact_us_form = forms.ContactUsForm()
        contact_us_form = forms.ContactUsModelForm()

    return render(request, 'contact_us_page.html', {'form': contact_us_form})
