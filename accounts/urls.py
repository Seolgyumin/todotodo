from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('onboarding/', views.onboarding, name='onboarding'),
    path('congrats/', views.congrats, name='congrats'),
    path('logout/', views.logout, name='logout'),
]
