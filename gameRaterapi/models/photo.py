from django.db import models
from .gamer import Gamer
from .game import Game

class Photo(models.Model):
    image = models.ImageField()
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)