from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from cnam.models import Cnammatriculecaisse, Cnamdetailsoin

class CnammatriculecaisseSerializer(ModelSerializer):
    class Meta:
        model = Cnammatriculecaisse
        fields = ('id','codeBureau','dateDossier','year', 'month', 'caisse','numeroDossier', 'dateSoins', 'caisseAssure', 'identifiantUniqueAssure', 'matriculeAssure',  'qualiteBeneficiaire','rangBeneficiaire', 'nomBeneficiaire', 'regime', 'etatDossier', 'decisionAdministrative', 'totalDepense', 'totalRembourse', 'referenceVir')

class CnamdetailsoinSerializer(ModelSerializer):
    class Meta:
        model = Cnamdetailsoin
        fields = ('id', 'codeBureau', 'dateDossier',  'numeroDossier', 'refernceBulletin',  'typeActe',  'description',  'nombre',   'dateActe',  'decision', 'montantDepense','montantReel','montantRembourse')
