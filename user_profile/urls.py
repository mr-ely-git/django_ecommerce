from django.urls import path
from user_profile import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page_url'),
]
