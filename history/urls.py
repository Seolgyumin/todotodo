from django.urls import path
from history import views

urlpatterns = [
    path('', views.index, name='history_index'),
]
