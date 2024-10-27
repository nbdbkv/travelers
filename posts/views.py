from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from posts.models import Country, Tag, Post
from posts.serializers import CountryListCreateSerializer, TagListCreateSerializer, PostSerializer


class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListCreateSerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListCreateSerializer
    permission_classes = (IsAuthenticated,)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if not user.is_anonymous:
            return queryset
        else:
            return queryset.order_by('-id')[:1]


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
