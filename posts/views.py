from django.db.models import Count
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from posts.models import Country, Tag, Post
from posts.serializers import CountrySerializer, CountryDetailSerializer, TagListCreateSerializer, PostSerializer


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
