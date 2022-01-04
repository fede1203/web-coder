from django.urls import path
from AppInicio import views


urlpatterns = [
    path('inicio', views.inicio ),
    path('base', views.base),
]
