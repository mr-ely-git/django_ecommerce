from django.urls import path
from . import views

urlpatterns = [
    # path('', views.contact_us_view, name='contact-us-url'),
    path('', views.ContactUsView.as_view(), name='contact-us-url'),
]
