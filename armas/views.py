from django.shortcuts import render, redirect, get_object_or_404
from .models import Arma
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate
from django.urls import reverse
from .models import Inventario
from .forms import ArmaForm, PasswordForm


@login_required
def lista_armas(request):
    query = request.GET.get("q", "")
    estado = request.GET.get("estado", "")
    tipo = request.GET.get("tipo", "")

    armas = Arma.objects.all()

    if query:
        armas = armas.filter(
            Q(codigo__icontains=query) |
            Q(serie__icontains=query)
        )
    if estado:
        armas = armas.filter(estado=estado)
    if tipo:
        armas = armas.filter(tipo=tipo)

    context = {
        "armas": armas,
        "estado": estado,
        "tipo": tipo,
        "query": query
    }
    return render(request, "armas/lista_armas.html", context)


@login_required
def registrar_arma(request):
    if request.method == 'POST':
        form = ArmaForm(request.POST, request.FILES)
        if form.is_valid():
            arma = form.save()
            # Guardar en inventario automáticamente
            Inventario.objects.create(arma=arma)
            return redirect('armas:lista_armas')
            # Aquí puedes agregar el registro al inventario si tienes ese modelo
            return redirect('armas:lista_armas')
    else:
        form = ArmaForm()
    return render(request, 'armas/registro_arma.html', {'form': form})


@login_required
def editar_arma(request, arma_id):
    arma = get_object_or_404(Arma, id=arma_id)

    if request.method == 'POST':
        pass_form = PasswordForm(request.POST)
        form = ArmaForm(request.POST, request.FILES, instance=arma)

        if pass_form.is_valid() and form.is_valid():
            password = pass_form.cleaned_data['password']
            user = authenticate(username=request.user.username, password=password)
            if user and user.is_superuser:
                form.save()
                return redirect('armas:lista_armas')
            else:
                form.add_error(None, 'Contraseña incorrecta o no eres administrador.')
    else:
        form = ArmaForm(instance=arma)
        pass_form = PasswordForm()

    return render(request, 'armas/editar_arma.html', {
        'form': form,
        'pass_form': pass_form,
        'arma': arma
    })




@login_required
def eliminar_arma(request, arma_id):
    arma = get_object_or_404(Arma, id=arma_id)
    if request.method == 'POST':
        arma.delete()
        return redirect('armas:lista_armas')
    return render(request, 'armas/confirmar_eliminacion.html', {'arma': arma})


@login_required
def detalle_arma(request, arma_id):
    arma = get_object_or_404(Arma, pk=arma_id)
    return render(request, 'armas/detalle_arma.html', {'arma': arma})








