from rest_framework import serializers

from posts.models import Country


class CountryListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha2Code', 'alpha3Code', 'capital', 'region')
