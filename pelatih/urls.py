from django.urls import path
from pelatih.views import *

app_name = 'pelatih'

urlpatterns = [
    path('daftar_atlet/', daftar_atlet, name='daftar_atlet'),
]