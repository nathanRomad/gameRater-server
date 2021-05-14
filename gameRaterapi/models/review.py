from django.db import models

class Review(models.Model):
    rating = models.IntegerField()
    review = models.CharField(max_length=140)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)