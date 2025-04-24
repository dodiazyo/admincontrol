from django.shortcuts import render, redirect, get_object_or_404
from .models import Oficial
from .forms import OficialForm
import openpyxl
from django.http import HttpResponse

# Registrar nuevo oficial
def registrar_oficial(request):
    if request.method == 'POST':
        form = OficialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_oficiales')
    else:
        form = OficialForm()
    return render(request, 'oficiales/registrar_oficial.html', {'form': form})

# Listado de oficiales
def lista_oficiales(request):
    oficiales = Oficial.objects.all()

    # Obtener valores del formulario GET
    estado = request.GET.get('estado')
    zona = request.GET.get('zona')
    turno = request.GET.get('turno')
    tipo_oficial = request.GET.get('tipo_oficial')

    # Aplicar filtros si están presentes
    if estado:
        oficiales = oficiales.filter(estado=estado)
    if zona:
        oficiales = oficiales.filter(zona=zona)
    if turno:
        oficiales = oficiales.filter(turno=turno)
    if tipo_oficial:
        oficiales = oficiales.filter(tipo_oficial=tipo_oficial)

    return render(request, 'oficiales/lista_oficiales.html', {'oficiales': oficiales})


# Editar oficial existente
def editar_oficial(request, oficial_id):
    oficial = get_object_or_404(Oficial, id=oficial_id)
    if request.method == 'POST':
        form = OficialForm(request.POST, request.FILES, instance=oficial)
        if form.is_valid():
            form.save()
            return redirect('lista_oficiales')
    else:
        form = OficialForm(instance=oficial)
    return render(request, 'oficiales/editar_oficial.html', {'form': form, 'oficial': oficial})

# Ver detalle de oficial
def ver_oficial(request, oficial_id):
    oficial = get_object_or_404(Oficial, id=oficial_id)
    return render(request, 'oficiales/detalle_oficial.html', {'oficial': oficial})

# Eliminar oficial con confirmación
def eliminar_oficial(request, oficial_id):
    oficial = get_object_or_404(Oficial, id=oficial_id)
    if request.method == 'POST':
        oficial.delete()
        return redirect('lista_oficiales')
    return render(request, 'oficiales/confirmar_eliminacion.html', {'oficial': oficial})




def exportar_oficiales_excel(request):
    oficiales = Oficial.objects.all()

    # Crear libro de Excel
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Oficiales"

    # Encabezados
    headers = [
        'ID Carnet', 'Nombre', 'Cédula', 'Estado', 'Ubicación', 'Zona',
        'Tipo', 'Turno', 'Fecha Ingreso', 'Tipo Oficial'
    ]
    ws.append(headers)

    # Agregar datos
    for oficial in oficiales:
        ws.append([
            oficial.id_carnet,
            oficial.nombre,
            oficial.cedula,
            oficial.estado,
            oficial.ubicacion,
            oficial.zona,
            oficial.tipo,
            oficial.turno,
            oficial.fecha_ingreso.strftime("%Y-%m-%d"),
            oficial.tipo_oficial,
        ])

    # Preparar respuesta
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=oficiales.xlsx'
    wb.save(response)
    return response

