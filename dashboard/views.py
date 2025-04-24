
from django.shortcuts import render
from armas.models import Arma
from oficiales.models import Oficial
from combustible.models import CargaCombustible



def index(request):
    context = {
        "total_armas": Arma.objects.count(),
        "total_oficiales": Oficial.objects.filter(estado="activo").count(),
        "total_combustible": CargaCombustible.objects.count()
    }
    return render(request, "dashboard/index.html", context)




