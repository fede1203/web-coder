from django.urls import path
from AppInicio import views


urlpatterns = [
    path('inicio', views.inicio, name= 'Inicio' ),
    path('base', views.base),
]
