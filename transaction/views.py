from django_filters.rest_framework.backends import DjangoFilterBackend
from transaction.models import Transactionsonede
from rest_framework import permissions, filters
from transaction.serializers import TransactionsonedeSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
# from audit.pagination import CustomPageNumberPagination


class TransactionsonedeAPIView(ListCreateAPIView):
    serializer_class = TransactionsonedeSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id','coderetour', 'reftrs','montant', 'date_trs','autorisation', 'status_trs' , 'partner' , 'card']
    search_fields = ['id', 'coderetour', 'reftrs','montant', 'date_trs','autorisation', 'status_trs' , 'partner' , 'card']
    ordering_fields = ['id', 'date_trs' ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Transactionsonede.objects.all()


class TransactionsonedeDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionsonedeSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "coderetour"

    def get_queryset(self):
        #return Facture.objects.filter(owner=self.request.user)
        return Transactionsonede.objects.filter(coderetour=self.kwargs['coderetour'])
