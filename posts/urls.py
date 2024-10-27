from django.urls import path

from posts.views import (
    CountryListView, CountryCreateView, CountryDetailView, TagListCreateView, PostListView, PostCreateView,
)

urlpatterns = [
    path('country/', CountryListView.as_view()),
    path('country/create/', CountryCreateView.as_view()),
    path('country/detail/<int:pk>/', CountryDetailView.as_view()),

    path('tag/', TagListCreateView.as_view()),

    path('post/', PostListView.as_view()),
    path('post/create/', PostCreateView.as_view()),
]
