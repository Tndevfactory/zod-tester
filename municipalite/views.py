from django_filters.rest_framework.backends import DjangoFilterBackend
from municipalite.models import Municipalite
from rest_framework import permissions, filters
from municipalite.serializers import MunicipaliteSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# from audit.pagination import CustomPageNumberPagination


class MunicipaliteAPIView(ListCreateAPIView):
    serializer_class = MunicipaliteSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'ref_STEG', 'label','ref_TT' ]
    search_fields = ['id', 'ref_STEG', 'label','ref_TT' ]
    ordering_fields = ['id', 'label' ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Municipalite.objects.all()


class MunicipaliteDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = MunicipaliteSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "label"

    def get_queryset(self):
        #return Facture.objects.filter(owner=self.request.user)
        return Municipalite.objects.filter(partner=self.kwargs['label'])
