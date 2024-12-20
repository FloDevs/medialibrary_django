from django.db import models
from .media_model import Media

class Book(Media):
    
    author = models.CharField(max_length=100)
   

    def __str__(self):
        return f"{self.author , self.name}"
