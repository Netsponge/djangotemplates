from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def accueil(request):
    return render(request, 'home.html')
