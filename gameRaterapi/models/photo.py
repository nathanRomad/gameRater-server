from django.db import models

class Photo(models.Model):
    image = models.URLField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)