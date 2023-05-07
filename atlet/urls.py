from django.urls import path
from atlet.views import *

app_name = 'atlet'

urlpatterns = [
    path('dashboard/', dashboard_atlet, name='dashboard_atlet'),
    path('enrolled_event/', enrolled_event, name='enrolled_event'),
    path('daftar_sponsor/', daftar_sponsor, name='daftar_sponsor')
]