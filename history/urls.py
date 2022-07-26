from django.urls import path
from history import views
from django.conf.urls import include


urlpatterns = [
    path('', views.index, name='history_index'),
    path('chat/', views.chat, name='chat'),
]
