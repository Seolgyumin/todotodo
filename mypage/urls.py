from django.urls import path
from mypage import views

app_name = 'mypage'
urlpatterns = [
    path('', views.index, name='mypage_index'),
    path('friends_list/', views.friends_list),
    path('add_persona/', views.add_persona),
    path('add_category/', views.add_category),
    path('add_friend/', views.add_friend),
]
