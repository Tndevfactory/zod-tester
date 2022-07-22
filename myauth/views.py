from django.shortcuts import render
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from myauth import serializers
from myauth.serializers import RegisterSerializer, LoginSerializer
from rest_framework import response, status, permissions, filters
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from myauth.models import User
from django_filters.rest_framework import DjangoFilterBackend


class AuthUserAPIView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return response.Response({'user': serializer.data})


class RegisterAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)

        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)


class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RegisterSerializer
    # permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return User.objects.filter(id=self.kwargs['id'])


class UserAPIView(ListCreateAPIView):
    serializer_class = RegisterSerializer
    # pagination_class = CustomPageNumberPagination
    # permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'username']
    search_fields = ['id', 'username' ]
    ordering_fields = ['id']

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return User.objects.all()
