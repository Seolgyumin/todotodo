from django.urls import path
from django.conf.urls import include
from todotodo import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('friend/<int:id>/', views.friend, name='friend'),
    path('accounts/', include('accounts.urls')),
    path('mypage/', include('mypage.urls')),
    path('alertcenter/', include('alertcenter.urls')),
    path('history/', include('history.urls')),
]
