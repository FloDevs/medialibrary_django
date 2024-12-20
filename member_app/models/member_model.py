from django.contrib.auth.models import User  
from django.db import models

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='member_profile')
    is_blocked = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.user.username} ({'Bloqué' if self.is_blocked else 'Actif'})"
