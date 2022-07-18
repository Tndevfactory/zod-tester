from django_filters.rest_framework.backends import DjangoFilterBackend
from cnrps.models import Assuree, Pension
from rest_framework import permissions, filters
from cnrps.serializers import AssureeSerializer, PensionSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# from audit.pagination import CustomPageNumberPagination


class AssureeAPIView(ListCreateAPIView):
    serializer_class = AssureeSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id',]
    search_fields = ['id',]
    ordering_fields = ['id', ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Assuree.objects.all()


class AssureeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AssureeSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "matricule"

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        print(self.kwargs['matricule'])
        return Assuree.objects.filter(partner=self.kwargs['matricule'])


class PensionAPIView(ListCreateAPIView):
    serializer_class = PensionSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', ]
    search_fields = ['id', ]
    ordering_fields = ['id', ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Pension.objects.all()


class PensionDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PensionSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "matricule"

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Pension.objects.filter(partner=self.kwargs['matricule'])
