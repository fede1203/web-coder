from django.urls import path
from AppHogar import views


urlpatterns = [
    path('blanco', views.blanco, name='Blanco' ),
    path('cocinas',views.cocinas, name='Cocinas'),
    path('electrodomesticos', views.electrodomesticos, name='Electrodomesticos'),


]
