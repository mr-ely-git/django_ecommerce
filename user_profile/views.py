from django.shortcuts import render
from django import views

from user_profile.forms import RegisterForm


# Create your views here.

class RegisterView(views.View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'register_page.html', context)

    def post(self, request):
        pass
