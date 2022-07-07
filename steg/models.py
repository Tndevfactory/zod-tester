import uuid

from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User

class Facture(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    dept = models.CharField(max_length=30)
    explanation = models.CharField(max_length=300)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
            return self.dept




