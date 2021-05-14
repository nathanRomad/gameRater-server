from django.db import models
from .game import Game
from .gamer import Gamer

class Review(models.Model):
    rating = models.IntegerField()
    review = models.CharField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)