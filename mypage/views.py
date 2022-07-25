from django.shortcuts import render
from todotodo.models import Persona

def index(request):
    personas = Persona.objects.all()
    return render(request, 'mypage/index.html', {'personas': personas})

def friends_list():
    return

def add_persona():
    return

def add_category():
    return

def add_friend():
    return

class FriendView:
    def delete():
        return

class FriendPersonaPermission:
    def create():
        return

    def delete():
        return