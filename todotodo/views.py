import os
from django.shortcuts import render, redirect
from .models import User, Persona
from django.views import View

# Create your views here.
def index(request):
    return render(request, 'todotodo/index.html')


def home(request):
    return render(request, 'todotodo/home.html')

def send_todo():
    return