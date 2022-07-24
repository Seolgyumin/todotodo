from tkinter import CASCADE
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Friendship(models.Model):
    friend1_id = models.ForeignKey(User, on_delete=models.CASCADE) #sender
    friend2_id = models.ForeignKey(User, on_delete=models.CASCADE) #receiver
    created_at = models.DateTimeField(default=timezone.now)

class Persona(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    message = models.TextField()
    # emozi = 
    created_at = models.DateTimeField(default=timezone.now)

class FriendshipRequest(models.Model):
    friend1_id = models.ForeignKey(User, on_delete=models.CASCADE) #sender
    friend2_id = models.ForeignKey(User, on_delete=models.CASCADE) #receiver
    persona1_ids = ArrayField(models.ForeignKey(Persona, on_delete=CASCADE)) #sender's open persona list
    persona2_ids = ArrayField(models.ForeignKey(Persona, on_delete=CASCADE)) #receiver's open persona list
    created_at = models.DateTimeField(default=timezone.now)

class PersonaPermission(models.Model):
    friendship_id = models.ForeignKey(Friendship, on_delete=CASCADE)
    persona_id = models.ForeignKey(Persona, on_delete=CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

class Category(models.Model):
    persona_id = models.ForeignKey(Persona, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    color = models.CharField(max_length=6) #settings.py의 hex code
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

class Todo(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    start_date = models.DateField(timezone.now)
    end_date = models.DateField(null=True, blank=True)
    sender_id = models.ForeignKey(User)

class TodoRequest(models.Model):
    sender_id = models.ForeignKey(User, on_delete=CASCADE)
    reciever_id = models.ForeignKey(User, on_delete=CASCADE)
    todo_name = models.CharField(max_length=256)
    todo_start_date = models.DateField(default=timezone.now)
    todo_end_date = models.DateField(null=True, blank=True)
    todo_id = models.ForeignKey(Todo, null=True, blank=True)
    status = models.IntegerField(MinValueValidator(0), MaxValueValidator(2))
    