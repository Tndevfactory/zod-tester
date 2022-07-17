from django_filters.rest_framework.backends import DjangoFilterBackend
from cnam.models import Cnammatriculecaisse, Cnamdetailsoin
from rest_framework import permissions, filters
from cnam.serializers import CnammatriculecaisseSerializer, CnamdetailsoinSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# from audit.pagination import CustomPageNumberPagination


class CnammatriculecaisseAPIView(ListCreateAPIView):
    serializer_class = CnammatriculecaisseSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'matriculeAssure', 'caisse', 'qualiteBeneficiaire', 'year', 'month']
    search_fields = ['id', 'matriculeAssure', 'caisse', 'qualiteBeneficiaire', 'year', 'month']
    ordering_fields = [ 'year', 'month']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Cnammatriculecaisse.objects.all()


class CnammatriculecaisseDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CnammatriculecaisseSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "matriculeAssure"

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Cnammatriculecaisse.objects.filter(partner=self.kwargs['matriculeAssure'])


class CnamdetailsoinAPIView(ListCreateAPIView):
    serializer_class = CnamdetailsoinSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'refernceBulletin']
    search_fields = ['id', 'refernceBulletin']
    ordering_fields = ['id', 'refernceBulletin']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Cnamdetailsoin.objects.all()


class CnamdetailsoinDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CnamdetailsoinSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "refernceBulletin"

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Cnamdetailsoin.objects.filter(partner=self.kwargs['refernceBulletin'])
