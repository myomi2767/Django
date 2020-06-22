from django.db import models

# Create your models here.
class Musician(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()

class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    # Musician의 1:N 관계
    title = models.CharField(max_length=150)