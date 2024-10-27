from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from posts.models import Country, Tag
from posts.serializers import CountryListCreateSerializer, TagListCreateSerializer


class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListCreateSerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagListCreateSerializer
    permission_classes = (IsAuthenticated,)
