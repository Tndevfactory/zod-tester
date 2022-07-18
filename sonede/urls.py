from sonede.views import FacturesonedeAPIView, FacturesonedeDetailAPIView
from django.urls import path

urlpatterns = [
    path("", FacturesonedeAPIView.as_view(), name="facture_sonede"),
    #services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    #path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    path("consultFactureAboBT/<str:reference>", FacturesonedeDetailAPIView.as_view(), name="factures_sonede_details")

]