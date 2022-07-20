from django.urls import path
from todotodo import views

urlpatterns = [
    path('', views.index, name='index'),
]