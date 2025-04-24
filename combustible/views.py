from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import CargaCombustibleForm
from .models import CargaCombustible

def registrar_carga(request):
    if request.method == 'POST':
        form = CargaCombustibleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('combustible:listado_cargas')
    else:
        form = CargaCombustibleForm()
    
    return render(request, 'combustible/registrar.html', {'form': form})


def listado_cargas(request):
    cargas = CargaCombustible.objects.all().order_by('-fecha')
    return render(request, 'combustible/listado.html', {'cargas': cargas})


from combustible.models import CargaCombustible

def index(request):
    cargas = CargaCombustible.objects.all()
    total_combustible = cargas.count()
    total_gasto = sum([c.total_pago() for c in cargas])
    promedio_rendimiento = (sum([c.rendimiento() for c in cargas]) / cargas.count()) if cargas.exists() else 0

    contexto = {
        'total_combustible': total_combustible,
        'total_gasto': total_gasto,
        'promedio_rendimiento': promedio_rendimiento,
    }

    return render(request, 'dashboard/index.html', contexto)
