from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User

class Facture(TrackingModel):
    dept = models.CharField(max_length=30)
    explanation = models.CharField(max_length=300)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
            return self.title





class Todo(TrackingModel):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    is_complete = models.BooleanField(default=False)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

