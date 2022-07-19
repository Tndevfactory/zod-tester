from django_filters.rest_framework.backends import DjangoFilterBackend
from sonede.models import Facturesonede
from rest_framework import permissions, filters
from sonede.serializers import FacturesonedeSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# from steg.pagination import CustomPageNumberPagination


class FacturesonedeAPIView(ListCreateAPIView):
    serializer_class = FacturesonedeSerializer
    #  pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'contractNumber', 'clientCode','invoiceRef' ]
    search_fields = ['id', 'contractNumber', 'clientCode', 'invoiceRef']
    ordering_fields = ['id', 'invoiceDate']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Facturesonede.objects.all()


class FacturesonedeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FacturesonedeSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "clientCode"

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Facturesonede.objects.filter(reference=self.kwargs['clientCode'])
