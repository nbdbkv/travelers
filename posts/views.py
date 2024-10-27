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


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated,)
