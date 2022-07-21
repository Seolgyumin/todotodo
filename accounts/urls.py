from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.index, name='account_index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
