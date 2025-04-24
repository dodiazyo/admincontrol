from django.urls import path
from . import views

app_name = 'combustible'

urlpatterns = [
    path('registrar/', views.registrar_carga, name='registrar_carga'),
    path('listado/', views.listado_cargas, name='listado_cargas'),
]
