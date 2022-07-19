import uuid

from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User


class Municipalite(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=200, null=True, blank=True)
    ref_STEG = models.CharField(max_length=200, null=True, blank=True)
    ref_TT = models.CharField(max_length=200, null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.label
