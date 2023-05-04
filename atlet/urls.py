from django.urls import path
from atlet.views import dashboard_atlet

app_name = 'atlet'

urlpatterns = [
    path('dashboard/', dashboard_atlet, name='dashboard_atlet'),
]