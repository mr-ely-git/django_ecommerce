from django.shortcuts import render
from django import views
from user_profile import forms


class RegisterView(views.View):
    def get(self, request):
        return render(request, 'register_page.html', {'register_form': forms.RegisterForm()})

    def post(self, request):
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            return render(request, 'register_page.html', {'register_form': forms.RegisterForm()})
        return render(request, 'register_page.html', {'register_form': register_form})
