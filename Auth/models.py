from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  level= models.IntegerField(default=1)
  xp= models.IntegerField(default=0)
