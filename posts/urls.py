from django.urls import path

from posts.views import CountryListCreateView

urlpatterns = [
    path('country/', CountryListCreateView.as_view()),
]
