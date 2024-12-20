from django.db import models

class Media(models.Model):
    name = models.CharField(max_length=200)
    loan_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
  

    class Meta:
        abstract = True 

    def __str__(self):
        return self.name
