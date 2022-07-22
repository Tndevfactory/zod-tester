from django_filters.rest_framework.backends import DjangoFilterBackend
from myadmin.models import Usermanage
from rest_framework import permissions, filters
from myadmin.serializers import UsermanageSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# from steg.pagination import CustomPageNumberPagination

class UsermanageAPIView(ListCreateAPIView):
    serializer_class = UsermanageSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'login', 'firstName','manisupality','lastName', 'email', 'imageUrl', 'activated', 'langKey' , 'createdBy' , 'createdDate']
    search_fields = ['id', 'login', 'firstName','manisupality','lastName', 'email', 'imageUrl', 'activated', 'langKey' , 'createdBy' , 'createdDate']
    ordering_fields = ['id']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Usermanage.objects.all()


class UsermanageDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UsermanageSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Usermanage.objects.filter(id=self.kwargs['id'])
