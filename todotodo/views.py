from re import I, L
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Persona, TodoRequest, Category, Todo, Friendship, PersonaPermission
from accounts.models import User
from django.utils import timezone
from datetime import date
import calendar as cd
from accounts.models import User
import json

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('todo:home')
    else:
        return render(request, 'todotodo/index.html')

def home(request):
    user = request.user
    if user.is_authenticated:
        personas = user.persona_set.all()
        persona_id = request.GET.get('persona_id')
        if persona_id:
            persona = Persona.objects.get(id=persona_id)
        else:
            persona = personas.first()
        persona_emoji = persona.emoji
        todorequests = TodoRequest.objects.filter(receiver_persona=persona)
        categories= persona.category_set.all()
        todos = dict()
        for category in categories:
            todos[str(category.name)]=category.todo_set.all().order_by('created_at')
        today=date.today()
        c=cd.Calendar(firstweekday=1)
        monthcal=[]
        weekcal=[]
        for i in c.monthdayscalendar(today.year,today.month):
            if today.day in i:
                weekcal = i
            monthcal.append(i)
        #personaid도 같이 render
        return render(request, 'todotodo/home.html', {'personas': personas, 'todorequests':todorequests, 'categories':categories, 'todos':sorted(todos.items()), 'weekcal':weekcal, 'monthcal':monthcal, 'persona':persona, 'todaydate':today.day, 'todaymonth':today.month, 'todayyear':today.year, 'persona_emoji':persona_emoji})
    else:
        return render(request, 'accounts/login_required.html')
# user_id, persona_id, my persona list, 날짜 정보, todo 및 카테고리

def friend(request, id, pid):
    friend = User.objects.get(id=id)
    friendship1 = Friendship.objects.filter(friend1=friend, friend2=request.user)
    friendship2 = Friendship.objects.filter(friend2=friend, friend1=request.user)
    #이거 역순도 고려해야함..
    friendship = friendship2 if friendship1 else friendship1
    personapermissions = friendship.personapermission_set.all()
    personas = Persona.objects.filter(personapermissions)
    persona = Persona.objects.get(id=pid)
    categories= persona.category_set.all()
    todos = dict()
    for category in categories:
        todos[str(category.name)] = category.todo_set.all()
    return render(request,'todotodo/freind.html', {'friend':friend, 'personas': personas, 'categories':categories, 'todos':sorted(todos.items())})



class PersonaView:
    def create(request):
        name = request.POST['name']
        persona = Persona.objects.create(user=request.user, name=name)
        return JsonResponse({'personaId': persona.id})

    def delete(request, id):
        persona = Persona.objects.get(id=id)
        persona.delete()
        return JsonResponse({})

    def edit(request, id):
        persona = Persona.objects.get(id=id)
        persona.name = request.POST['name']
        persona.save()
        return JsonResponse({'updatePersonaName':persona.name})
    



class CategoryView:
    def create(request, id):
        name=request.POST['name']
        persona=Persona.objects.get(id=id)
        category = Category.objects.create(persona=persona, name=name)
        return JsonResponse({'personaId': persona.id, 'categoryId': category.id, 'categoryCreatedAt': category.created_at})

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
        todo = Todo.objects.create(category=category, start_date=timezone.now(), end_date=end_date, name=name, sender=request.user)
        return JsonResponse({'todoId':todo.id, 'todoEndDate':todo.end_date})
    
    def delete(request, id):
        todo = Todo.objects.get(id=id)
        todo.delete()
        return JsonResponse({})

    def edit(request, id):
        todo = Todo.objects.get(id=id)
        todo.name = request.POST['name']
        todo.save()
        return JsonResponse({'updateTodoName':todo.name})

    def complete(request, id):
        todo = Todo.objects.get(id=id)
        if todo.completed:
            todo.completed = False
        else:
            todo.completed = True
        todo.save()
        return JsonResponse({
            "is_completed": todo.completed
        })