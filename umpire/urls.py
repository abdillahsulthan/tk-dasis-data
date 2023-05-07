from django.urls import path
from umpire.views import *

app_name = 'umpire'

urlpatterns = [
    path('list_event/', list_event, name='list_event')
]