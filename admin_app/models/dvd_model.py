from django.db import models
from .media_model import Media

class Dvd(Media):
    
    director = models.CharField(max_length=100)
    

   