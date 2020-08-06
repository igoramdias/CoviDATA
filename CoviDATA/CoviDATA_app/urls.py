from django.urls import path
from CoviDATA_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('numcasos/', views.numcasos, name='numcasos'),
    path('analicasos/', views.analicasos, name='analicasos'),
    path('controlgastos/', views.controlgastos, name='controlgastos'),
]