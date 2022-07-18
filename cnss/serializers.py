from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from cnss.models import Releve


class ReleveSerializer(ModelSerializer):
    class Meta:
        model = Releve
        fields = ('id', 'rownum', 'matricule','cle', 'annee', 'salaire' , 'classe', 'assure' , 'employeur')