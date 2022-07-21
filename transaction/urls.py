from transaction.views import TransactionsonedeAPIView, TransactionsonedeDetailAPIView
from django.urls import path

urlpatterns = [
    path("transaction", TransactionsonedeAPIView.as_view(), name="transaction"),
    #services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    #path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    path("getTransactionDetails", TransactionsonedeDetailAPIView.as_view(), name="getTransactionDetails")

]