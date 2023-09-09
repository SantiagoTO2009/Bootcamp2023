from django.shortcuts import render
from .models import Cancion

def detalle_cancion(request, cancion_id):
    cancion = Cancion.objects.get(id=cancion_id)
    return render(request, 'musica/detalle_cancion.html', {'cancion': cancion})
