from cnss.views import ReleveAPIView, ReleveDetailAPIView
from django.urls import path

urlpatterns = [
    path("releve", ReleveAPIView.as_view(), name="releveAPIView"),
    #services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    #path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    path("cnssReleve/<str:reference>", ReleveDetailAPIView.as_view(), name="releveDetailAPIView")

]