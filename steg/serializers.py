from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from steg.models import Facture, Paiementfacture
import base64

class FactureSerializer(ModelSerializer):
    class Meta:
        model = Facture
        fields = ('id', 'reference', 'etatEnc', 'etat', 'derniereFacture')


class PaiementfactureSerializer(ModelSerializer):
    class Meta:
        model = Paiementfacture
        fields = ('id', 'reftrs', 'qrcode')

        def get_qrcode_image(self, place):
            img = open(self.qrcode.path, "rb")
            data = img.read()
            return "data:image/jpg;base64,%s" % data.encode('base64')
