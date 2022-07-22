import uuid

from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User


class Usermanage(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    authorities = models.JSONField(null=True, blank=True)
    activated = models.CharField(max_length=200, null=True, blank=True)
    login = models.CharField(max_length=160,null=True, blank=True)
    firstName = models.CharField(max_length=200, null=True, blank=True)
    lastName = models.CharField(max_length=200, null=True, blank=True)
    manisupality = models.CharField(max_length=200, null=True, blank=True)
    imageUrl = models.CharField(max_length=200, null=True, blank=True)
    langKey = models.CharField(max_length=200, null=True, blank=True)
    createdBy = models.CharField(max_length=200, null=True, blank=True)
    createdDate = models.CharField(max_length=200, null=True, blank=True)
    lastModifiedBy = models.CharField(max_length=200, null=True, blank=True)
    lastModifiedDate = models.CharField(max_length=200, null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
            return self.lastName




