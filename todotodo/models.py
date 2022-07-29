from django.db import models
from django.utils import timezone
from accounts.models import User, Friendship
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Persona(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=dict)
    name = models.CharField(max_length=256, default='')
    emoji = models.TextField(max_length=256, default='')
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

class PersonaPermission(models.Model):
    friendship = models.ForeignKey(Friendship, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

class Category(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default='')
    color = models.CharField(max_length=7, default='#DDDDDD') #settings.py의 hex code
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    @receiver(post_save, sender=Persona)  
    def create_default_category(sender, instance, created, **kwargs):        
        if created:          
            Category.objects.create(persona=instance, name="Routine")  
    
class Todo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default='')
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False) 

class TodoRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todo_sender', default=dict)
    receiver_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='todo_receiver_persona', default=dict)
    todo_name = models.CharField(max_length=256)
    todo_start_date = models.DateField(default=timezone.now)
    todo_end_date = models.DateField(null=True, blank=True)
    todo = models.ForeignKey(Todo, null=True, blank=True, on_delete=models.CASCADE)
    status = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(2)])
    message = models.TextField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
