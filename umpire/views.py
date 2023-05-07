from django.shortcuts import render

# Create your views here.
def list_event(request):
    return render(request, "list_event.html")