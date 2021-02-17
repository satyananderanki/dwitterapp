from django.db import models
from django.contrib.auth.models import User


class Dweet(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    content = models.TextField(max_length=150)
    likes = models.IntegerField(blank=True, null=True)


class Comments(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=150)
    connected_post = models.ForeignKey(Dweet, on_delete=models.CASCADE)


class Follow(models.Model):
    owner = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    target_owner = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

# Create your models here.
