from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='search-home'),
    path('result/', views.result, name='search-result'),
    path('search-form/', views.search_form, name='search_form'),
    path('search/', views.search_form, name='search'),
]
