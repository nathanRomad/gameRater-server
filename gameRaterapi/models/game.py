from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    maker = models.CharField(max_length=50)
    releaseYear = models.IntegerField()
    numberOfPlayers = models.IntegerField()
    estTime = models.IntegerField()
    ageRecommendation = models.IntegerField()