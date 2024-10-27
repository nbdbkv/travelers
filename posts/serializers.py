from rest_framework import serializers

from posts.models import Country, Tag, Post


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha2Code', 'alpha3Code', 'capital', 'region')


class TagListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('id', 'topic', 'description', 'user', 'country', 'tag')


class PostDetailSerializer(serializers.ModelSerializer):
    tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('id', 'topic', 'description', 'tag')


class CountryDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(source='country_posts', many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha2Code', 'alpha3Code', 'capital', 'region', 'posts')
