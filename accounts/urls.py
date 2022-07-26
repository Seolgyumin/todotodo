from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('congrats/', views.congrats, name='congrats'),
]
