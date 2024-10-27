from rest_framework import serializers

from posts.models import Country, Tag


class CountryListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha2Code', 'alpha3Code', 'capital', 'region')


class TagListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')
