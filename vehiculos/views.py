from django.shortcuts import render, redirect
from .models import Vehiculo, ChequeoDiario
from .forms import VehiculoForm, ChequeoDiarioForm
from django.shortcuts import render, get_object_or_404
from combustible.models import CargaCombustible


def registrar_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = VehiculoForm()
    return render(request, 'vehiculos/registro.html', {'form': form})

def lista_vehiculos(request):
    tipo = request.GET.get('tipo')
    if tipo:
        vehiculos = Vehiculo.objects.filter(tipo=tipo)
    else:
        vehiculos = Vehiculo.objects.all()
    tipos = Vehiculo.objects.values_list('tipo', flat=True).distinct()
    return render(request, 'vehiculos/lista.html', {
        'vehiculos': vehiculos,
        'tipos': tipos,
        'tipo_seleccionado': tipo
    })



def registrar_chequeo(request):
    if request.method == 'POST':
        form = ChequeoDiarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_vehiculos')
    else:
        form = ChequeoDiarioForm()
    return render(request, 'vehiculos/registro_chequeo.html', {'form': form})


def historial_chequeo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    chequeos = ChequeoDiario.objects.filter(vehiculo=vehiculo).order_by('-fecha')
    return render(request, 'vehiculos/historial_chequeo.html', {
        'vehiculo': vehiculo,
        'chequeos': chequeos
    })



def detalle_vehiculo(request, vehiculo_id):
    vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
    chequeos = ChequeoDiario.objects.filter(vehiculo=vehiculo).order_by('-fecha')[:5]
    cargas = CargaCombustible.objects.filter(vehiculo=vehiculo).order_by('-fecha')[:5]

    contexto = {
        'vehiculo': vehiculo,
        'chequeos': chequeos,
        'cargas': cargas,
    }
    return render(request, 'vehiculos/detalle.html', contexto)



def lista_vehiculos(request):
    tipo = request.GET.get('tipo')
    if tipo:
        vehiculos = Vehiculo.objects.filter(tipo=tipo)
    else:
        vehiculos = Vehiculo.objects.all()
    tipos = Vehiculo.objects.values_list('tipo', flat=True).distinct()
    return render(request, 'vehiculos/lista.html', {
        'vehiculos': vehiculos,
        'tipos': tipos,
        'tipo_seleccionado': tipo
    })




