from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from telecom.models import Facturetelecom


class FacturetelecomSerializer(ModelSerializer):
    class Meta:
        model = Facturetelecom
        fields = ('id', 'reference', 'etatEnc','etat', 'derniereFacture')