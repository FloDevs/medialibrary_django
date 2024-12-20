from django.db import models
from .media_model import Media

class Cd(Media):
    
    artist = models.CharField(max_length=100)
