from django.urls import path

from accounts.views import UserRegisterView, UserVerifyView

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('verify/', UserVerifyView.as_view()),
]
