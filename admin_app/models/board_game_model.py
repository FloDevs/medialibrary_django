from django.db import models

class BoardGame(models.Model):
    name = models.CharField(max_length=200)
    creator = models.CharField(max_length=100)

    def __str__(self):
        return self.name