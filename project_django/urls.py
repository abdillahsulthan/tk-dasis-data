from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('atlet/', include('atlet.urls')),
    path('', include('authentication.urls')),
    path('umpire/', include('umpire.urls')),
    path('pelatih/', include('pelatih.urls')),
]
