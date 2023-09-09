from django.urls import path
from . import views

urlpatterns = [
    path('cancion/<int:cancion_id>/', views.detalle_cancion, name='detalle_cancion'),
    # Otras URL para tus vistas
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('musica/', include('musica.urls')),
    # Otras URL del proyecto principal
]
