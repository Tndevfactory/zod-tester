from django_filters.rest_framework.backends import DjangoFilterBackend
from telecom.models import Facturetelecom
from rest_framework import permissions, filters
from telecom.serializers import FacturetelecomSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
#from steg.pagination import CustomPageNumberPagination


class FacturetelecomAPIView(ListCreateAPIView):
    serializer_class = FacturetelecomSerializer
    #pagination_class = CustomPageNumberPagination
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
        return Facturetelecom.objects.all()


class FacturetelecomDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FacturetelecomSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "reference"

    def get_queryset(self):
        #return Facture.objects.filter(owner=self.request.user)
        return Facturetelecom.objects.filter(reference=self.kwargs['reference'])
