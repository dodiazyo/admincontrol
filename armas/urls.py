
# armas/urls.py
from django.urls import path
from . import views
from .views import lista_armas, registrar_arma, editar_arma, eliminar_arma, detalle_arma

app_name = 'armas'

urlpatterns = [
    path('', lista_armas, name='lista_armas'),  # ✅ Esto carga con /armas/
    path('registrar/', registrar_arma, name='registrar_arma'),
    path('editar/<int:arma_id>/', editar_arma, name='editar_arma'),
    path('eliminar/<int:arma_id>/', eliminar_arma, name='eliminar_arma'),
    path('detalle/<int:arma_id>/', detalle_arma, name='detalle_arma'),
    path('', views.lista_armas, name='lista_armas'),

]



