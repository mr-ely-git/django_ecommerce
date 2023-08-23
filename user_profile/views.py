from django.shortcuts import render
from django import views
from django.utils.crypto import get_random_string

from user_profile import forms
from django.contrib.auth.models import User
from . import models


class RegisterView(views.View):
    def get(self, request):
        return render(request, 'register_page.html', {'register_form': forms.RegisterForm()})

    def post(self, request):
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password')
            is_registered = User.objects.filter(email__iexact=email).exists()
            if is_registered:
                register_form.add_error('email', 'ایمیل قبلا ثبت شده است')
            else:
                new_user = User(email=email)
                new_user.set_password(password)
                new_user.save()
                models.UserInformation.objects.create(user=new_user, email_activation_code=get_random_string(120))
                # fixme : create and redirect to login page instead render register_page.html
                return render(request, 'register_page.html', {'register_form': forms.RegisterForm()})

        return render(request, 'register_page.html', {'register_form': register_form})
