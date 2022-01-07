from django.urls import path
from AppInicio import views as viewsInicio
from AppHogar import views 




urlpatterns = [
    path('inicio', viewsInicio.inicio, name= 'Inicio' ),
    path('blanco', views.blanco, name='Blanco' ),
 
]
