from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from transaction.models import Transactionsonede


class TransactionsonedeSerializer(ModelSerializer):
    class Meta:
        model = Transactionsonede
        fields = ('id', 'coderetour', 'card' , 'partner' , 'reftrs','montant', 'date_trs','autorisation', 'status_trs')
