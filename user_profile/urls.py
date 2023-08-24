from django.urls import path
from user_profile import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page_url'),
    path('login/', views.LoginView.as_view(), name='login_page_url'),
    path('activate_account/<str:email_activation_code>', views.ActivateAccountView.as_view(), name='activate_account_page_url'),
]
