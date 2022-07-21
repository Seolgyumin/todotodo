from django.urls import path
from alertcenter import views

urlpatterns = [
    path('', views.index, name='alertcenter_index'),
]
