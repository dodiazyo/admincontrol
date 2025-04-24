from django.urls import path
from .views import registrar_vehiculo, lista_vehiculos
from .views import registrar_vehiculo, lista_vehiculos, registrar_chequeo
from . import views

app_name = 'vehiculos'
urlpatterns = [
    path('registrar/', registrar_vehiculo, name='registrar_vehiculo'),
    path('lista/', lista_vehiculos, name='lista_vehiculos'),
    path('chequeo/', registrar_chequeo, name='registrar_chequeo'),
    path('detalle/<int:vehiculo_id>/', views.detalle_vehiculo, name='detalle_vehiculo'),
    


]

