from django.urls import path
from django.conf.urls import include
from todotodo import views

app_name = "todo"
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('mypage/', include('mypage.urls')),
    path('history/', include('history.urls')),
    path('alertcenter/', include('alertcenter.urls')),
    path('send_todo/', views.send_todo),
]
