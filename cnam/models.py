from django.db import models
# Create your models here.
import uuid
from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User

class Cnammatriculecaisse(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    codeBureau = models.CharField(max_length=100, null=True, blank=True)
    dateDossier = models.CharField(max_length=100, null=True, blank=True)
    year = models.CharField(max_length=100, null=True, blank=True)
    month = models.CharField(max_length=100, null=True, blank=True)
    caisse = models.CharField(max_length=100, null=True, blank=True)
    numeroDossier = models.CharField(max_length=100, null=True, blank=True)
    dateSoins = models.CharField(max_length=100, null=True, blank=True)
    caisseAssure = models.CharField(max_length=100, null=True, blank=True)
    identifiantUniqueAssure = models.CharField(max_length=100, null=True, blank=True)
    matriculeAssure = models.CharField(max_length=100, null=True, blank=True)
    qualiteBeneficiaire = models.CharField(max_length=100, null=True, blank=True)
    rangBeneficiaire = models.CharField(max_length=100, null=True, blank=True)
    nomBeneficiaire = models.CharField(max_length=100, null=True, blank=True)
    regime = models.CharField(max_length=100, null=True, blank=True)
    etatDossier = models.CharField(max_length=100, null=True, blank=True)
    decisionAdministrative = models.CharField(max_length=100, null=True, blank=True)
    totalDepense = models.CharField(max_length=100, null=True, blank=True)
    totalRembourse = models.CharField(max_length=100, null=True, blank=True)
    referenceVir = models.CharField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.caisse


class Cnamdetailsoin(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    codeBureau = models.CharField(max_length=100, null=True, blank=True)
    dateDossier = models.CharField(max_length=100, null=True, blank=True)
    numeroDossier = models.CharField(max_length=100, null=True, blank=True)
    refernceBulletin = models.CharField(max_length=100, null=True, blank=True)
    typeActe = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    dateActe = models.CharField(max_length=100, null=True, blank=True)
    decision = models.CharField(max_length=100, null=True, blank=True)
    montantDepense = models.CharField(max_length=100, null=True, blank=True)
    montantReel = models.CharField(max_length=100, null=True, blank=True)
    montantRembourse = models.CharField(max_length=100, null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.typeActe