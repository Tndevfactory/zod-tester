from municipalite.views import MunicipaliteAPIView, MunicipaliteDetailAPIView
from django.urls import path

urlpatterns = [
    path("", MunicipaliteAPIView.as_view(), name="municipaliteAPIView"),
    #services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    #path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    path("municipalite", MunicipaliteDetailAPIView.as_view(), name="municipaliteDetailAPIView")

]