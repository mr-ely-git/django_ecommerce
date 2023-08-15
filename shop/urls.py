from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index_page_view, name='index-page-url'),
    path('', views.IndexPageView.as_view(), name='index-page-url'),
    path('shop/', views.shop_page_view, name='shop-page-url'),
    path('shop/<slug>', views.single_page_view, name='single-page-url'),
]
