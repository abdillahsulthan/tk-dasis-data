from django.urls import path
from atlet.views import *

app_name = 'atlet'

urlpatterns = [
    path('dashboard/', dashboard_atlet, name='dashboard_atlet'),
    path('enrolled_event/', enrolled_event, name='enrolled_event'),
    path('daftar_sponsor/', daftar_sponsor, name='daftar_sponsor'),
    path('input_data_kualifikasi/', input_data_kualifikasi, name='input_data_kualifikasi'),
    path('kategori_partner/', kategori_partner, name='kategori_partner'),
    path('daftar_event1/', daftar_event1, name='daftar_event1'),
    path('daftar_event2/', daftar_event2, name='daftar_event2'),
    path('pertanyaan_kualifikasi/', pertanyaan_kualifikasi, name='pertanyaan_kualifikasi')
]