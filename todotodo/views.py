from re import I, L
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Persona, TodoRequest, User, Category, Todo, Friendship, PersonaPermission
from django.utils import timezone
from datetime import date
import calendar as cd
import json

# Create your views here.
def index(request):
    return render(request, 'todotodo/index.html')

def home(request, id):
    personas = request.user.persona_set.all()
    todorequests = TodoRequest.objects.filter(receiver_id=request.user)
    #이거 todorequest 불러오는거 request.user를 receiver로 설정해야한느데..
    persona = Persona.objects.get(id=id)
    categories= persona.category_set.all()
    todos = dict()
    for category in categories:
        todos[str(category.name)]=category.todo_set.all()
    today=date.today()
    c=cd.Calendar(firstweekday=1)
    monthcal=[]
    weekcal=[]
    for i in c.monthdayscalendar(today.year,today.month):
        if today.day in i:
            weekcal = i
        monthcal.append(i)
    #personaid도 같이 render
    return render(request, 'todotodo/home.html', {'personas': personas, 'todorequests':todorequests, 'categories':categories, 'todos':sorted(todos.items()), 'weekcal':weekcal, 'monthcal':monthcal, 'persona':persona})
# user_id, persona_id, my persona list, 날짜 정보, todo 및 카테고리

def friend(request, id, pid):
    friend_id = User.objects.get(id=id).id
    friendship1 = Friendship.objects.filter(friend1_id=friend_id, friend2_id=request.user.id)
    friendship2 = Friendship.objects.filter(friend2_id=friend_id, friend1_id=request.user.id)
    #이거 역순도 고려해야함..
    friendship = friendship2 if friendship1 else friendship1
    personapermissions = friendship.personapermission_set.all()
    personas = Persona.objects.filter(personapermissions)
    persona = Persona.objects.get(id=pid)
    categories= persona.category_set.all()
    todos = dict()
    for category in categories:
        todos[str(category.name)] = category.todo_set.all()
    return render(request,'todotodo/freind.html', {'friend_id':friend_id, 'personas': personas, 'categories':categories, 'todos':sorted(todos.items())})



class PersonaView:
    def create(request):
        name=request.POST['name']
        persona = Persona.objects.create(name=name, user_id=request.user)
        return JsonResponse({
            'personaId': persona.id,
            'personaName': name,
            'personaCreatedAt':persona.created_at,
            'success': True
            })

    def delete(request, id):
        persona = Persona.objects.get(id=id)
        persona.delete()
        return JsonResponse({
            'success': True,
        })

    def edit(request, id):
        persona = Persona.objects.get(id=id)
        persona.update(name=request.POST['name'])
        return JsonResponse({
            'updatePersonaName': persona.name,
            'success': True
            })


class CategoryView:
    def create(request, id):
        name=request.POST['name']
        category = Category.objects.create(persona_id=id, name=name)
        return JsonResponse({'personaId': id, 'categoryId':category.id, 'categoryCreatedAt':category.created_at})

    def delete(request, id):
        category = Category.objects.get(id=id)
        category.delete()
        return JsonResponse({})

    def edit(request, id):
        category = Category.objects.get(id=id)
        category.update(name=request.POST['name'])
        return JsonResponse({'updateCategoryName':category.name})

class TodoView:
    def create(request, id):
        end_date=request.POST['end_date']
        name=request.POST['name']
        category = Category.objects.get(id=id)
        todo = Todo.objects.create(category_id=category, start_date=timezone.now(), end_date=end_date, name=name, sender_id=request.user)
        return JsonResponse({'todoId':todo.id, 'todoEndDate':todo.end_date})
    
    def delete(request, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return JsonResponse({})

    def edit(request, id):
        todo = Todo.objects.get(id=id)
        todo.update(name=request.POST['name'], end_date=request.POST['end_date'])
        return JsonResponse({'updateTodoName':todo.name, 'updateTodoEndDate':todo.end_date})
