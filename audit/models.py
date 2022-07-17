import uuid

from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User


class Audit(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=20)
    user = models.CharField(max_length=70)
    partner = models.CharField(max_length=80)
    createdAt = models.CharField(max_length=80)
    montant = models.CharField(max_length=80, null=True, blank=True)
    type = models.CharField(max_length=20, null=True, blank=True)
    entries = models.CharField(max_length=200)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.partner
