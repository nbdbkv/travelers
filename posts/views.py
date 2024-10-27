from django.db.models import Count
from rest_framework import generics
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated

from posts.models import Country, Tag, Post, PostImage
from posts.serializers import (
    CountrySerializer, CountryDetailSerializer, TagListCreateSerializer, PostListSerializer, PostCreateSerializer,
    PostImageCreateSerializer,
)


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        queryset = Country.objects.annotate(post_count=Count('country_posts')).filter(post_count__gt=0)
        return queryset


class CountryCreateView(generics.CreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetailView(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryDetailSerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListCreateSerializer
    permission_classes = (IsAuthenticated,)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.filter(is_shown=True)
    serializer_class = PostListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = super().get_queryset()
        if not user.is_anonymous:
            return queryset
        else:
            return queryset.order_by('-id')[:10]


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = (IsAuthenticated,)


class PostImageCreateView(generics.CreateAPIView):
    queryset = PostImage.objects.all()
    serializer_class = PostImageCreateSerializer
    parser_classes = (FormParser, MultiPartParser)
    permission_classes = (IsAuthenticated,)
