from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from todotodo.models import Friendship

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=256, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField('self', through=Friendship, related_name='friendship')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
