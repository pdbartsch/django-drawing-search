from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='search-home'),
    path('about/', views.about, name='search-about'),
    path('result/', views.result, name='search-result'),
]