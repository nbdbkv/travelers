from rest_framework import generics

from posts.models import Country
from posts.serializers import CountryListCreateSerializer


class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryListCreateSerializer
