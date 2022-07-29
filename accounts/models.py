from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    kakao_id = models.IntegerField(blank=True, null=True)
    thumbnail_img = models.TextField(verbose_name='썸네일 이미지 URL', blank=True, null=True)
    onboarding_done = models.BooleanField(default=False)
    connected_at = models.DateTimeField(default=timezone.now)

class Friendship(models.Model):
    friend1_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_sender')
    friend2_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_receiver')
    created_at = models.DateTimeField(default=timezone.now)


class FriendshipRequest(models.Model):
    friend1_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_request_sender')
    friend2_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_request_receiver')
    persona1_ids = models.JSONField(default=dict) #sender's open persona list
    created_at = models.DateTimeField(default=timezone.now)
