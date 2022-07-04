from steg.views import StegAPIView, StegDetailAPIView
from django.urls import path

urlpatterns = [
    path("", StegAPIView.as_view(), name="stegs"),
    path("<int:id>", StegDetailAPIView.as_view(), name="steg")
]