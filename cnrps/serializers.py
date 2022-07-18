from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from cnrps.models import Assuree, Pension

class AssureeSerializer(ModelSerializer):
    class Meta:
        model = Assuree
        fields = ('id','cin','dateAf','dateFinContrat', 'dateNaissance', 'etatAffiliation','libCodePos', 'libModeRecrut', 'matricule', 'modRecru', 'nom',  'position','prenom', 'sexe')

class PensionSerializer(ModelSerializer):
    class Meta:
        model = Pension
        fields = ('id', 'matricule', 'lit',  'prenom', 'nom',  'datePaie',  'dateNais',  'etatAffiliation',   'cin',  'libModeRecrut')
