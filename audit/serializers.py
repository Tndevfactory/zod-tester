from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from audit.models import Audit


class AuditSerializer(ModelSerializer):
    class Meta:
        model = Audit
        fields = ('id', 'ip', 'user','partner', 'createdAt','montant', 'type', 'entries')
