from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import (
    UserListView, UserRegisterView, UserVerifyView, ProfileView, ProfileUpdateView, TokenAccessView,
)

urlpatterns = [
    path('', UserListView.as_view()),

    path('register/', UserRegisterView.as_view()),
    path('verify/', UserVerifyView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('profile/update/', ProfileUpdateView.as_view()),
    path('token/access/', TokenAccessView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
