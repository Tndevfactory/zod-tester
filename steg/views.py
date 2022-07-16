from django_filters.rest_framework.backends import DjangoFilterBackend
from steg.models import Facture
from rest_framework import permissions, filters
from steg.serializers import FactureSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from steg.pagination import CustomPageNumberPagination


class StegAPIView(ListCreateAPIView):
    serializer_class = FactureSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'reference' ]
    search_fields = ['id', 'reference' ]
    ordering_fields = ['id', 'reference' ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Facture.objects.all()


class StegDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FactureSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "reference"

    def get_queryset(self):
        #return Facture.objects.filter(owner=self.request.user)
        return Facture.objects.filter(reference=self.kwargs['reference'])
