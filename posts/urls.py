from django.urls import path

from posts.views import CountryListCreateView, TagListCreateView, PostListView, PostCreateView

urlpatterns = [
    path('country/', CountryListCreateView.as_view()),

    path('tag/', TagListCreateView.as_view()),

    path('post/', PostListView.as_view()),
    path('post/create/', PostCreateView.as_view()),
]
