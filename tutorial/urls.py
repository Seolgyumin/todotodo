from django.urls import path
from django.conf.urls import include
from tutorial import views

urlpatterns = [
    path('', views.index, name='tutorial_index'),
    path('name/', views.name),
    path('email/', views.email),
    path('password/', views.password),
    path('photo/', views.photo),
    path('set_mypage/'), include('mypage.urls'),
    path('welcome/', views.welcome),
    ]