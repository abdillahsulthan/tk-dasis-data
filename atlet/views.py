from django.shortcuts import render

# Create your views here.
def dashboard_atlet(request):
    return render(request, "dashboard.html")