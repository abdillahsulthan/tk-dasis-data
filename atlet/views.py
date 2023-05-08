from django.shortcuts import render

# Create your views here.
def dashboard_atlet(request):
    return render(request, "dashboard.html")

def enrolled_event(request):
    return render(request, "enrolled_event.html")

def daftar_sponsor(request):
    return render(request, "daftar_sponsor.html")

def daftar_event1(request):
    return render(request, "daftar_event1.html")

def daftar_event2(request):
    return render(request, "daftar_event1.html")

def pertanyaan_kualifikasi(request):
    return render(request, "pertanyaan_kualifikasi.html")

def input_data_kualifikasi(request):
    return render(request, "input_data_kualifikasi.html")

def kategori_partner(request):
    return render(request, "kategori_partner.html")