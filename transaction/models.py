import uuid

from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User


class Transactionsonede(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    coderetour = models.CharField(max_length=60, null=True, blank=True)
    reftrs = models.CharField(max_length=80, null=True, blank=True)
    montant = models.CharField(max_length=280, null=True, blank=True)
    card = models.CharField(max_length=280, null=True, blank=True)
    partner = models.CharField(max_length=280, null=True, blank=True)
    date_trs = models.CharField(max_length=80, null=True, blank=True)
    autorisation = models.CharField(max_length=80, null=True, blank=True)
    status_trs = models.CharField(max_length=20, null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.coderetour
