from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models.member_model import Member

# Crée automatiquement un profil Member lorsque l'utilisateur est créé
@receiver(post_save, sender=User)
def create_member_profile(sender, instance, created, **kwargs):
    if created:  # Si l'utilisateur est nouvellement créé
        Member.objects.create(user=instance)  # Crée un profil lié au User

# Sauvegarde le profil Member lorsque le User est modifié
@receiver(post_save, sender=User)
def save_member_profile(sender, instance, **kwargs):
    instance.member_profile.save()
