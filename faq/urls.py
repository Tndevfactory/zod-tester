from faq.views import FaqAPIView, FaqDetailAPIView
from django.urls import path

urlpatterns = [
    path("faq", FaqAPIView.as_view(), name="faq"),
    #path("faqdetails", FaqDetailAPIView.as_view(), name="faqdetails"),

    # services/microservice1/api/consultFactureAboBT/<int:id>?username=admin

    # path("getAssureByMatricule/<matricule>", AssureeDetailAPIView.as_view(), name="getAssureByMatricule"),
    # path("getAssureByCinDateNais/<str:cin>/<str:dateNaissance>", AssureeDetailAPIView.as_view(), name="getAssureByCinDateNais"),

    # path("getPensionneByMatricule/<str:matricule>", PensionDetailAPIView.as_view(), name="getPensionneByMatricule"),
    # path("getPensionneByCinDateNais/<str:cin>/<str:dateNais>", PensionDetailAPIView.as_view(),name="getPensionneByCinDateNais")
    # path("getBulletinSoinsByMatriculeAndCaisse", CnammatriculecaisseDetailAPIView.as_view(), name="Cnammatriculecaissedetail"),

    # path("getBulletinSoinsDetails/{refernceBulletin}", CnamdetailsoinAPIView.as_view(), name="cnamdetailsoin"),
    # services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    # path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    # path("getBulletinSoinsDetails/{refernceBulletin}", CnamdetailsoinDetailAPIView.as_view(), name="cnamdetailsoindetail"),

]
