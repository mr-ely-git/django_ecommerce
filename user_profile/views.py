from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
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
                new_user = User(email=email, username=email, is_active=False)
                new_user.set_password(password)
                new_user.save()
                models.UserInformation.objects.create(user=new_user, email_activation_code=get_random_string(120))

                return redirect(reverse('login_page_url'))

        return render(request, 'register_page.html', {'register_form': register_form})


class LoginView(views.View):
    def get(self, request):
        return render(request, 'login_page.html', {'login_form': forms.LoginForm()})

    def post(self):
        pass


class ActivateAccountView(views.View):
    def get(self, request, email_activation_code):
        user_info: models.UserInformation = models.UserInformation.objects.filter(
            email_activation_code__iexact=email_activation_code).first()

        if user_info is not None:
            user = user_info.user
            if not user.is_active:
                user.is_active = True
                user.save()
                user_info.email_activation_code = get_random_string(120)
                user_info.save()
                # fixme : show success message
                return redirect(reverse('login_page_url'))
            else:
                # fixme : user already active
                pass
        else:
            raise Http404
