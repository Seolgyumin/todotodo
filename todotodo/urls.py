from django.urls import path
from django.conf.urls import include
from todotodo import views

app_name = "todo"
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('<int:id>/friend/<int:pid>/', views.friend, name='friend'),
    path('createpersona/', views.PersonaView.create, name='persona-create'),
    path('deletepersona/<int:id>/', views.PersonaView.delete, name='persona-delete'),
    path('editpersona/<int:id>/', views.PersonaView.edit, name='persona-edit'),
    path('createcategory/<int:id>/', views.CategoryView.create, name='category-create'),
    path('deletecategory/<int:id>/', views.CategoryView.delete, name='categoty-delete'),
    path('editcategory/<int:id>/', views.CategoryView.edit, name='category-edit'),
    path('createtodo/<int:id>/', views.TodoView.create, name='todo-create'),
    path('deletetodo/<int:id>/', views.TodoView.delete, name='todo-delete'),
    path('edittodo/<int:id>/', views.TodoView.edit, name='todo-edit'),
    path('accounts/', include('accounts.urls')),
    path('mypage/', include('mypage.urls')),
    path('alertcenter/', include('alertcenter.urls')),
    path('history/', include('history.urls')),
    path('completetodo/<int:id>/', views.TodoView.complete, name='todo_complete'),
]
