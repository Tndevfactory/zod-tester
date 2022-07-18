from django_filters.rest_framework.backends import DjangoFilterBackend
from faq.models import Faq
from rest_framework import permissions, filters
from faq.serializers import FaqSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend


# from audit.pagination import CustomPageNumberPagination


class FaqAPIView(ListCreateAPIView):
    serializer_class = FaqSerializer
    # pagination_class = CustomPageNumberPagination
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['id','question', 'reponse']
    search_fields = ['id','question', 'reponse']
    ordering_fields = ['id','question' ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        return Faq.objects.all()


class FaqDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = FaqSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "question"

    def get_queryset(self):
        # return Facture.objects.filter(owner=self.request.user)
        print(self.kwargs['question'])
        return Faq.objects.filter(partner=self.kwargs['question'])
