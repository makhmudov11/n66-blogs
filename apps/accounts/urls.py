from django.urls import path

from apps.accounts.views import RegisterCreateAPIView, LoginAPIView, NewAccessToken, UserProfileAPIView

urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('refresh/', NewAccessToken.as_view()),
    path('profile/', UserProfileAPIView.as_view()),
]