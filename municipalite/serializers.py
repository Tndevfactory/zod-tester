from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from municipalite.models import Municipalite


class MunicipaliteSerializer(ModelSerializer):
    class Meta:
        model = Municipalite
        fields = ('id', 'ref_STEG', 'label','ref_TT')
