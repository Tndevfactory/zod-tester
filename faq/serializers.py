from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from faq.models import Faq

class FaqSerializer(ModelSerializer):
    class Meta:
        model = Faq
        fields = ('id','question','reponse')

