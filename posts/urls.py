from django.urls import path

from posts.views import (
    CountryListView, CountryCreateView, CountryDetailView, TagListCreateView, PostListView, PostCreateView,
    PostImageCreateView, CommentCreateView,
)

urlpatterns = [
    path('country/', CountryListView.as_view()),
    path('country/create/', CountryCreateView.as_view()),
    path('country/detail/<int:pk>/', CountryDetailView.as_view()),

    path('tag/', TagListCreateView.as_view()),

    path('', PostListView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('create/image/', PostImageCreateView.as_view()),
    path('create/comment/', CommentCreateView.as_view()),
]
