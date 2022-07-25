from django.shortcuts import render
from todotodo.models import Persona

def index(request):
    personas = Persona.objects.all()
    return render(request, 'mypage/index.html', {'personas': personas})

def friends_list(request):
    return render(request, 'mypage/friends_list.html')

def add_persona():
    return

def add_category():
    return

def add_friend():
    return