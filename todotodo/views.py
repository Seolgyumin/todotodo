from django.shortcuts import render
from .models import Persona

# Create your views here.

def index(request):
    personas = Persona.objects.all()
    return render(request, 'todotodo/index.html', {'personas': personas})

def home(request):
    return

def send_todo():
    return
