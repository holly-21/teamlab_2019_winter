from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('list/', views.list, name='list'),
    path('search/result', views.result, name='result'),
]