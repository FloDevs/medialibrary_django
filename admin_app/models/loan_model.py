from django.db import models
from django.contrib.auth.models import User  
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from datetime import timedelta

class Loan(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)  
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    media = GenericForeignKey('content_type', 'object_id')
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)

    def clean(self):
        """ Logique de validation de l'emprunt """
        current_loans_count = Loan.objects.filter(member=self.member, return_date__isnull=True).count()
        if current_loans_count >= 3:
            raise ValidationError(f"L'utilisateur {self.member.username} a déjà 3 emprunts en cours.")

        overdue_loans = Loan.objects.filter(
            member=self.member,
            return_date__isnull=True,
            loan_date__lt=now().date() - timedelta(days=7)
        )
        if overdue_loans.exists():
            raise ValidationError(f"L'utilisateur {self.member.username} a des emprunts en retard.")

        if self.member.member_profile.is_blocked:
            raise ValidationError(f"L'utilisateur {self.member.username} est bloqué et ne peut pas emprunter.")

        if self.content_type.model == 'boardgame':
            raise ValidationError("Les jeux de plateau ne peuvent pas être empruntés.")

        if hasattr(self.media, 'is_available') and not self.media.is_available:
            raise ValidationError(f"Le média {self.media} n'est pas disponible à l'emprunt.")

    def save(self, *args, **kwargs):
        self.clean()
        if hasattr(self.media, 'is_available'):
            self.media.is_available = False
            self.media.save()
        super().save(*args, **kwargs)

    def return_media(self):
        """ Marquer l'emprunt comme retourné """
        self.return_date = now().date()
        if hasattr(self.media, 'is_available'):
            self.media.is_available = True
            self.media.save()
        self.save()

    def __str__(self):
        return f'{self.media} emprunté par {self.member.username}'
