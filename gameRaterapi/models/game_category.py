from gameRaterapi.models.category import Category
from gameRaterapi.models.game import Game
from django.db import models

class GameCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)