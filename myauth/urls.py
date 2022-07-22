from myauth import views
from django.urls import path

urlpatterns = [
    path('register', views.RegisterAPIView.as_view(), name="register"),
    path('authenticate', views.LoginAPIView.as_view(), name="login"),
   # path('user', views.AuthUserAPIView.as_view(), name="user"),
    path('user', views.UserAPIView.as_view(), name="user"),
    path('user/<int:id>', views.UserDetailAPIView.as_view(), name="details_user"),
]