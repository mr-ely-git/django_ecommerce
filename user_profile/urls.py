from django.urls import path
from user_profile import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page_url'),
    path('activate-account/<str:email_activation_code>', views.ActivateAccountView.as_view(),
         name='activate_account_page_url'),
    path('login/', views.LoginView.as_view(), name='login_page_url'),
    path('forget-password/', views.ForgetPassword.as_view(), name='forget_password_page_url'),
    path('reset-password/<str:password_reset_code>', views.ResetPassword.as_view(), name='reset_password_page_url'),

]
