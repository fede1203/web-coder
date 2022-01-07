from django.urls import path
from AppHogar import views


urlpatterns = [
    path('blanco', views.blanco, name='Blanco' ),
    path('cocinas',views.cocinas, name='Cocinas'),
    path('electrodomesticos', views.electrodomesticos, name='Electrodomesticos'),
    path('blancoForm', views.blancoForm, name='BlancoForm' ),
    path('cocinaForm', views.cocinaForm, name='CocinasForm' ),
    path('electroForm', views.electroForm, name='ElectroForm' ),
    

    

]
