from django.urls import path
from applications.account.views import RegisterView, ActivationAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('sign-in/', TokenObtainPairView.as_view()),
    path('sign-out/', TokenRefreshView.as_view()),
    path('activate/<uuid:activation_code>', ActivationAPIView.as_view()),
    path('sign-up/', RegisterView.as_view())
]