from django.db import models


# Create your models here.
class Facture(models.Model):
    dept = models.CharField(max_length=30)
    explanation = models.CharField(max_length=300)
