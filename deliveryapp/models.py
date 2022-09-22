from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class userdata(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
