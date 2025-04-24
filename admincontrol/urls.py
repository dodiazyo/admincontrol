from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('oficiales/', include('oficiales.urls')),
    path('vehiculos/', include('vehiculos.urls')),
    path('login/', include('usuarios.urls')),  # ✅ Login principal
    path('', include('dashboard.urls')),       # ✅ Dashboard principal
    path('armas/', include('armas.urls')),     # ✅ Armas correctamente
    path('armas/', include('armas.urls', namespace='armas')),
      # ... otros paths
    path('combustible/', include('combustible.urls', namespace='combustible')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


