from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Zod API",
        default_version='v1',
        description="Created by developer Chawki au sein de E-solution TACTIC, interface de test api , juillet-2022",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@tndev-art.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[]
)

urlpatterns = [

    path('swagger.json', schema_view.without_ui( cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),

    # auth gateway
    path("api/", include("myauth.urls")),

    # microservice prepended with the name steg services/microservice1/api/
    path("steg/services/microservice1/api/", include("steg.urls")),
    path("cnam/services/microservice1/api/", include("cnam.urls")),
    path("audit/services/microservice1/api/", include("audit.urls")),
    path("cnrps/services/microservice1/api/", include("cnrps.urls")),
    path("cnss/services/microservice1/api/", include("cnss.urls")),
    path("faq/services/microservice1/api/", include("faq.urls")),
    path("sonede/services/microservice1/api/", include("sonede.urls")),
    path("telecom/services/microservice1/api/", include("telecom.urls")),
    path("municipalite/services/microservice1/api/", include("municipalite.urls")),
    path("transaction/services/microservice1/api/", include("transaction.urls")),
    path("myadmin/api/admin/", include("myadmin.urls")),
    # path("cnss/services/microservice1/api/", include("steg.urls")),

    # users managment
    # path("cnss/services/microservice1/api/", include("steg.urls")),

]
