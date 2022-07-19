from rest_framework import fields
from rest_framework.serializers import ModelSerializer
from myadmin.models import Usermanage


class UsermanageSerializer(ModelSerializer):
    class Meta:
        model = Usermanage
        fields = ('id', 'login', 'firstName','manisupality','lastName', 'email', 'imageUrl', 'activated', 'langKey' , 'createdBy' , 'createdDate' , 'lastModifiedBy' , 'lastModifiedDate', 'authorities')