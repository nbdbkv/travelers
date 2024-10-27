from django.urls import path

from accounts.views import UserRegisterView, UserVerifyView, ProfileView, ProfileUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('verify/', UserVerifyView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('profile/update/', ProfileUpdateView.as_view()),
]
