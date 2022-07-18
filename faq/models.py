from django.db import models
# Create your models here.
import uuid
from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User

class Faq(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=700, null=True, blank=True)
    reponse = models.CharField(max_length=1000, null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.question
