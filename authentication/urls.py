from django.urls import path
from authentication.views import show_homepage,show_login, show_register

app_name = 'authentication'

urlpatterns = [
    path('', show_homepage, name='show_homepage'),
    path('login/', show_login, name='show_login'),
    path('register/', show_register, name='show_register' ),
]