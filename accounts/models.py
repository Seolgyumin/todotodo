from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class KakaoUser(models.Model):
    name = models.CharField(max_length=256, default='', verbose_name='사용자명')
    email = models.EmailField(max_length=256, verbose_name='사용자이메일', blank=True, null=True)
    thumbnail_image_url = models.TextField(verbose_name='썸네일 이미지 URL', blank=True, null=True)
    profile_image_url = models.TextField(verbose_name='썸네일 이미지 URL', blank=True, null=True)
    connected_at = models.DateTimeField(default=timezone.now)

class Profile(models.Model):
    name = models.CharField(max_length=256, default='')
    user = models.OneToOneField(KakaoUser, on_delete=models.CASCADE)
    friends = models.ManyToManyField("self", symmetrical=False, through="todotodo.Friendship", related_name='friendship')
    created_at = models.DateTimeField(default=timezone.now)

    @receiver(post_save, sender=User)  
    def create_user_profile(sender, instance, created, **kwargs):        
        if created:          
            Profile.objects.create(user=instance)  
    
    @receiver(post_save, sender=User)  
    def save_user_profile(sender, instance, **kwargs):        
        instance.profile.save()