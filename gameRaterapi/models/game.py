from django.db import models
from .category import Category
from .game_category import GameCategory

class Game(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=140)
    maker = models.CharField(max_length=50)
    releaseYear = models.IntegerField()
    number_of_players = models.IntegerField()
    est_time = models.IntegerField()
    age_recommendation = models.IntegerField()
    categories = models.ManyToManyField("Category", through="GameCategory")