from django.db import models
from django.utils import timezone
from accounts.models import KakaoUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Friendship(models.Model):
    friend1_id = models.ForeignKey(KakaoUser, on_delete=models.CASCADE, related_name='friendship_sender')
    friend2_id = models.ForeignKey(KakaoUser, on_delete=models.CASCADE, related_name='friendship_receiver')
    created_at = models.DateTimeField(default=timezone.now)

class Persona(models.Model):
    user_id = models.ForeignKey(KakaoUser, on_delete=models.CASCADE, default=dict)
    name = models.CharField(max_length=256, default='')
    message = models.TextField()
    # emozi = 
    created_at = models.DateTimeField(default=timezone.now)

class FriendshipRequest(models.Model):
    friend1_id = models.ForeignKey(KakaoUser, on_delete=models.CASCADE, related_name='friendship_request_sender')
    friend2_id = models.ForeignKey(KakaoUser, on_delete=models.CASCADE, related_name='friendship_request_receiver')
    persona1_ids = models.JSONField(default=dict) #sender's open persona list
    created_at = models.DateTimeField(default=timezone.now)

class PersonaPermission(models.Model):
    friendship_id = models.ForeignKey(Friendship, on_delete=models.CASCADE)
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

class Category(models.Model):
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default='')
    color = models.CharField(max_length=7, default='#DDDDDD') #settings.py의 hex code
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

class Todo(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default='')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    sender_id = models.ForeignKey(KakaoUser, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)

class TodoRequest(models.Model):
    sender_id = models.ForeignKey(KakaoUser, on_delete=models.CASCADE, related_name='todo_sender', default=dict)
    receiver_id = models.ForeignKey(KakaoUser, on_delete=models.CASCADE, related_name='todo_receiver', default=dict)
    todo_name = models.CharField(max_length=256)
    todo_start_date = models.DateField(default=timezone.now)
    todo_end_date = models.DateField(null=True, blank=True)
    todo_id = models.ForeignKey(Todo, null=True, blank=True, on_delete=models.CASCADE)
    status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    message = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
