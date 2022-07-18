import uuid

from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User

class Releve(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    rownum = models.CharField(max_length=6, null=True, blank=True)
    matricule = models.CharField(max_length=50, null=True, blank=True)
    cle = models.CharField(max_length=8, null=True, blank=True)
    annee = models.CharField(max_length=18, null=True, blank=True)
    salaire = models.CharField(max_length=98, null=True, blank=True)
    classe = models.CharField(max_length=98, null=True, blank=True)
    assure = models.JSONField(null=True, blank=True)
    employeur = models.JSONField(null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
            return self.matricule
