from django.shortcuts import render
from .models import Persona

# Create your views here.
def index(request):
    return render(request, 'todotodo/index.html')

def home(request):
    return

def send_todo():
    return
