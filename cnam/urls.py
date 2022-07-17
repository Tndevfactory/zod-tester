from cnam.views import CnammatriculecaisseAPIView, CnammatriculecaisseDetailAPIView, CnamdetailsoinAPIView, \
    CnamdetailsoinDetailAPIView
from django.urls import path

urlpatterns = [
    path("getBulletinSoinsByMatriculeAndCaisse", CnammatriculecaisseAPIView.as_view(), name="Cnammatriculecaisse"),
    path("getBulletinSoinsDetails/{refernceBulletin}", CnamdetailsoinAPIView.as_view(), name="cnamdetailsoin")
    # services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    # path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    # path("getBulletinSoinsByMatriculeAndCaisse", CnammatriculecaisseDetailAPIView.as_view(), name="Cnammatriculecaissedetail"),

    # path("getBulletinSoinsDetails/{refernceBulletin}", CnamdetailsoinAPIView.as_view(), name="cnamdetailsoin"),
    # services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    # path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    # path("getBulletinSoinsDetails/{refernceBulletin}", CnamdetailsoinDetailAPIView.as_view(), name="cnamdetailsoindetail"),

]
