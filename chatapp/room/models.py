from django.contrib.auth.models import User
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        ordering = ('date_added',)


class Reactions(models.Model):
    messageid = models.ForeignKey(Message, related_name='messages', on_delete=models.CASCADE)
    reaction = models.CharField(max_length=5)
