from audit.views import AuditAPIView, AuditDetailAPIView
from django.urls import path

urlpatterns = [
    path("", AuditAPIView.as_view(), name="audits"),
    #services/microservice1/api/consultFactureAboBT/<int:id>?username=admin
    #path("<int:id>/microservice1?user=admin", StegDetailAPIView.as_view(), name="steg")
    path("audit", AuditDetailAPIView.as_view(), name="audit")

]