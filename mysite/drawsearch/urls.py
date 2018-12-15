from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='search-home'),
    path('result/', views.result, name='search-result'),
    path('search/', views.search, name='search'),
]
