from rest_framework import serializers
from myauth.models import User


class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff', 'is_superuser' , 'is_active', 'date_joined', 'email_verified',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User

        fields = ('id', 'email', 'username', 'password', 'is_staff', 'is_superuser' , 'is_active', 'date_joined', 'email_verified',  'token')

        read_only_fields = ['token']