from django_filters.rest_framework.backends import DjangoFilterBackend
from cnss.models import Releve
from rest_framework import permissions, filters
from cnss.serializers import ReleveSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# from audit.pagination import CustomPageNumberPagination


class ReleveAPIView(ListCreateAPIView):
    serializer_class = ReleveSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id', 'matricule','cle', 'annee', 'salaire' , 'classe']
    search_fields = ['id', 'matricule','cle', 'annee', 'salaire' , 'classe'  ]
    ordering_fields = ['id', 'annee']

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Releve.objects.all()


class ReleveDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReleveSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "matricule"

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        print(self.kwargs['matricule'])
        return Releve.objects.filter(partner=self.kwargs['matricule'])


