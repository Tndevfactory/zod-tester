from myadmin.views import UsermanageDetailAPIView, UsermanageAPIView
from django.urls import path

urlpatterns = [
    path("users", UsermanageAPIView.as_view(), name="user"),
    #services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    #path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    path("users/<int:id>", UsermanageDetailAPIView.as_view(), name="user_details")

]