from django_filters.rest_framework.backends import DjangoFilterBackend
from audit.models import Audit
from rest_framework import permissions, filters
from audit.serializers import AuditSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# from audit.pagination import CustomPageNumberPagination


class AuditAPIView(ListCreateAPIView):
    serializer_class = AuditSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'partner' ]
    search_fields = ['id', 'partner' ]
    ordering_fields = ['id', 'partner' ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Audit.objects.all()


class AuditDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AuditSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "partner"

    def get_queryset(self):
        #return Facture.objects.filter(owner=self.request.user)
        return Audit.objects.filter(partner=self.kwargs['partner'])
