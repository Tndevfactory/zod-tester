from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from steg.models import Facture


class FactureSerializer(ModelSerializer):
    class Meta:
        model = Facture
        fields = ('dept', 'explanation',)