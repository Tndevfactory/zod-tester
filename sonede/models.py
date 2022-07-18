import uuid

from django.db import models
from myhelpers.models import TrackingModel
from myauth.models import User

class Facturesonede(TrackingModel):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id = models.AutoField(primary_key=True)
    billerAuthId = models.CharField(max_length=60, null=True, blank=True)
    billerMf = models.CharField(max_length=60, null=True, blank=True)
    invoiceRef = models.CharField(max_length=60, null=True, blank=True)
    ttnRef = models.CharField(max_length=60, null=True, blank=True)
    contractNumber = models.CharField(max_length=60, null=True, blank=True)
    clientCode = models.CharField(max_length=60, null=True, blank=True)
    clientCin = models.CharField(max_length=60, null=True, blank=True)
    clientPassport = models.CharField(max_length=60, null=True, blank=True)
    clientCs = models.CharField(max_length=60, null=True, blank=True)
    clientMf = models.CharField(max_length=60, null=True, blank=True)
    clientName = models.CharField(max_length=60, null=True, blank=True)
    clientLastname = models.CharField(max_length=60, null=True, blank=True)
    clientRs = models.CharField(max_length=60, null=True, blank=True)
    clientPhones = models.CharField(max_length=60, null=True, blank=True)
    clientEmails = models.CharField(max_length=60, null=True, blank=True)
    invoiceTaxAmount = models.CharField(max_length=60, null=True, blank=True)
    invoiceOriginalAmount = models.CharField(max_length=60, null=True, blank=True)
    invoiceAmount = models.CharField(max_length=60, null=True, blank=True)
    invoiceDate = models.CharField(max_length=60, null=True, blank=True)
    invoiceExpiryDate = models.CharField(max_length=60, null=True, blank=True)
    invoiceAttachments = models.CharField(max_length=60, null=True, blank=True)
    paymentStatus = models.CharField(max_length=60, null=True, blank=True)
    invoicePreiod = models.JSONField(null=True, blank=True)
    invoiceDetails = models.JSONField(null=True, blank=True)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
            return self.clientCode


