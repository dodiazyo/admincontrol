
from django.urls import path
from .views import (
    registrar_oficial,
    lista_oficiales,
    editar_oficial,
    ver_oficial,           # 👈 Asegúrate de incluir esta
    eliminar_oficial,       # 👈 Y esta si la estás usando
    ver_oficial, eliminar_oficial, exportar_oficiales_excel  # 👈 Agrega esto
)

urlpatterns = [
    path('registrar/', registrar_oficial, name='registrar_oficial'),
    path('lista/', lista_oficiales, name='lista_oficiales'),
    path('editar/<int:oficial_id>/', editar_oficial, name='editar_oficial'),
    path('detalle/<int:oficial_id>/', ver_oficial, name='ver_oficial'),
    path('eliminar/<int:oficial_id>/', eliminar_oficial, name='eliminar_oficial'),
    path('exportar/', exportar_oficiales_excel, name='exportar_oficiales'),
]

