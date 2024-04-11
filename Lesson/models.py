from django.db import models
from django.utils.timezone import now

# Create your models here.
class Lesson(models.Model):

  class Difficulty(models.TextChoices):
    EASY = "1", "Facile"
    NORMAL = "2", "Moyen"
    HARD = "3", "Difficile"
    EXTREM = "4", "Exteme"

  title = models.CharField(default="Titre du cours", max_length=100)
  description = models.CharField(default="Description du cours", max_length=300)
  author = models.CharField(max_length=10)
  dificulty = models.CharField(max_length=2,
        choices=Difficulty.choices,
        default=Difficulty.EASY)
  xp_reward = models.IntegerField(default=25)
  created_at = models.DateTimeField(default=now)
  updated_at = models.DateTimeField(default=now)

class Chapiter(models.Model):
  title = models.CharField(default="Titre du chapitre", max_length=100)
  content = models.TextField(default="Contenue du chapitre", max_length=3000)
  lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
  created_at = models.DateTimeField(default=now)
  updated_at = models.DateTimeField(default=now)
