from django.db import models
# Create your models here.
import uuid
from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User

class Assuree(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    cin = models.CharField(max_length=100, null=True, blank=True)
    dateAf = models.CharField(max_length=100, null=True, blank=True)
    dateFinContrat = models.CharField(max_length=100, null=True, blank=True)
    dateNaissance = models.CharField(max_length=100, null=True, blank=True)
    etatAffiliation = models.CharField(max_length=100, null=True, blank=True)
    libCodePos = models.CharField(max_length=100, null=True, blank=True)
    libModeRecrut = models.CharField(max_length=100, null=True, blank=True)
    matricule = models.CharField(max_length=100, null=True, blank=True)
    modRecru = models.CharField(max_length=100, null=True, blank=True)
    nom = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    sexe = models.CharField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.matricule


class Pension(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    matricule = models.CharField(max_length=100, null=True, blank=True)
    lit = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    nom = models.CharField(max_length=100, null=True, blank=True)
    datePaie = models.CharField(max_length=100, null=True, blank=True)
    dateNais = models.CharField(max_length=100, null=True, blank=True)
    etatAffiliation = models.CharField(max_length=100, null=True, blank=True)
    cin = models.CharField(max_length=100, null=True, blank=True)
    libModeRecrut = models.CharField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.matricule