from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('congrats/', views.congrats, name='congrats'),
]
