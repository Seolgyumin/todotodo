from django.urls import path
from mypage import views
import todotodo.views

app_name = 'mypage'
urlpatterns = [
    path('', views.index, name='mypage_index'),
    path('friends_list/', views.friends_list),
    path('add_persona/', views.add_persona),
    path('add_category/', views.add_category),
    path('add_friend/', views.add_friend),
    path('createpersona/', todotodo.views.PersonaView.create),
    path('editpersona/', todotodo.views.PersonaView.edit),
    path('deletepersona/', todotodo.views.PersonaView.delete),
]
