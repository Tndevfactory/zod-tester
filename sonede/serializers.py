from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from sonede.models import Facturesonede


class FacturesonedeSerializer(ModelSerializer):
    class Meta:
        model = Facturesonede
        fields = ('id', 'billerAuthId', 'billerMf','invoiceRef', 'ttnRef', 'contractNumber', 'clientCode', 'clientCin' , 'clientPassport' , 'clientCs' , 'clientMf' , 'clientName', 'clientLastname', 'clientRs', 'clientPhones', 'clientEmails', 'invoiceTaxAmount' , 'invoiceOriginalAmount' , 'invoiceAmount' , 'invoiceDate' , 'invoiceExpiryDate', 'invoiceAttachments','invoicePreiod', 'invoiceDetails', 'paymentStatus')