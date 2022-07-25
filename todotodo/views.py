from django.shortcuts import render
from .models import Persona

# Create your views here.

def index(request):
    personas = Persona.objects.all()
    return render(request, 'todotodo/index.html', {'personas': personas})

def home(request):
    return render(request, 'todotodo/home.html')

def send_todo():
    return