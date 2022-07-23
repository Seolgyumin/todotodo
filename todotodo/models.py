from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Friendship(models.Model):
    friend1_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_sender') #sender
    friend2_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_receiver') #receiver
    created_at = models.DateTimeField(default=timezone.now)

class Persona(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=256, default='')
    message = models.TextField()
    # emozi = 
    created_at = models.DateTimeField(default=timezone.now)

class FriendshipRequest(models.Model):
    friend1_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_request_sender') #sender
    friend2_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_request_receiver') #receiver
    persona1_ids = models.ManyToManyField(Persona, related_name='sender_persona_open') #sender's open persona list
    persona2_ids = models.ManyToManyField(Persona, related_name='receiver_persona_open') #receiver's open persona list
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
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)

class TodoRequest(models.Model):
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_sender', default=1)
    reciever_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_receiver', default=1)
    todo_name = models.CharField(max_length=256, default='')
    todo_start_date = models.DateField(default=timezone.now)
    todo_end_date = models.DateField(null=True, blank=True)
    todo_id = models.ForeignKey(Todo, null=True, blank=True, on_delete=models.CASCADE)
    status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    created_at = models.DateTimeField(default=timezone.now)
    