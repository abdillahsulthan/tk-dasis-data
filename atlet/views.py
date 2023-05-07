from django.shortcuts import render

# Create your views here.
def dashboard_atlet(request):
    return render(request, "dashboard.html")

def enrolled_event(request):
    return render(request, "enrolled_event.html")

def daftar_sponsor(request):
    return render(request, "daftar_sponsor.html")