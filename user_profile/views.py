from django.contrib.auth import login, logout
from django.http import Http404, HttpRequest
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


class LoginView(views.View):
    def get(self, request):
        return render(request, 'login_page.html', {'login_form': forms.LoginForm()})

    def post(self, request: HttpRequest):
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                if user.is_active:
                    if user.check_password(password):
                        login(request, user)
                        return redirect(reverse('index-page-url'))
                    else:
                        login_form.add_error('email', 'نام کاربردی یا رمز عبور اشتباه است.')

                else:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است.')
            else:
                login_form.add_error('email', 'نام کاربردی یا رمز عبور اشتباه است.')

        return render(request, 'login_page.html', {'login_form': login_form})


class ForgetPassword(views.View):
    def get(self, request: HttpRequest):
        return render(request, 'forget_password_page.html', {'forget_form': forms.ForgetPasswordForm()})

    def post(self, request: HttpRequest):
        forget_form = forms.ForgetPasswordForm(request.POST)
        if forget_form.is_valid():
            email = forget_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=email)
            if user is not None:
                # fixme : send email
                pass
            else:
                forget_form.add_error('email', 'کاربری با این ایمیل پیدا نشد.')
        return render(request, 'forget_password_page.html', {'forget_form': forget_form})


class ResetPassword(views.View):
    def get(self, request: HttpRequest, password_reset_code):
        user: User = User.objects.filter(userinformation__email_activation_code__iexact=password_reset_code).first()
        if user is not None:
            return render(request, 'reset_password_page.html', {'reset_form': forms.ResetPasswordForm()})
        else:
            return redirect(reverse('register_page_url'))
