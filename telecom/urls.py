from telecom.views import FacturetelecomAPIView, FacturetelecomDetailAPIView
from django.urls import path

urlpatterns = [
    path("", FacturetelecomAPIView.as_view(), name="FacturetelecomAPIView"),
    #services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    #path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    path("consultFacturetelecom/<str:reference>", FacturetelecomDetailAPIView.as_view(), name="facturetelecomDetailAPIView")

]