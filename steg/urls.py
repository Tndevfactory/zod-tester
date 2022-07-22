from steg.views import StegAPIView, StegDetailAPIView, PaiementfactureAPIView
from django.urls import path

urlpatterns = [
    path("", StegAPIView.as_view(), name="stegs"),
    #services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    #path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    path("consultFactureAboBT/<str:reference>", StegDetailAPIView.as_view(), name="steg"),
    path("getQrcode", PaiementfactureAPIView.as_view(), name="qrcodesteg")

]