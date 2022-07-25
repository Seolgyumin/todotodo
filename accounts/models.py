from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from todotodo.models import Friendship
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=256, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField("self", symmetrical=False, through=Friendship, related_name='friendship')
    created_at = models.DateTimeField(default=timezone.now)

    @receiver(post_save, sender=User)  
    def create_user_profile(sender, instance, created, **kwargs):        
        if created:          
            Profile.objects.create(user=instance)  
    
    @receiver(post_save, sender=User)  
    def save_user_profile(sender, instance, **kwargs):        
        instance.profile.save()