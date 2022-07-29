from django.shortcuts import render
from todotodo.models import Persona, Category

def index(request):
    user = request.user
    personas = Persona.objects.filter(user=user)
    persona_categories = []

    for persona in personas:
        each = {}
        each['persona'] = persona
        each['categories'] = Category.objects.filter(persona=persona)
        persona_categories.append(each)

    print(persona_categories)
    return render(request, 'mypage/index.html', {'personas': persona_categories})

def friends_list(request):
    return render(request, 'mypage/friends_list.html')

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