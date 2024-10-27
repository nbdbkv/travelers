from django.urls import path

from posts.views import CountryListCreateView, TagListCreateView

urlpatterns = [
    path('country/', CountryListCreateView.as_view()),

    path('tag/', TagListCreateView.as_view()),
]
