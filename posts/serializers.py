from rest_framework import serializers

from posts.models import Country, Tag, Post, PostImage


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha2Code', 'alpha3Code', 'capital', 'region')


class TagListCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ('id', 'image')


class PostListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)
    post_images = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'topic', 'description', 'user', 'country', 'tag', 'post_images')


class PostCreateSerializer(serializers.ModelSerializer):
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
    posts = PostDetailSerializer(source='country_posts', many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha2Code', 'alpha3Code', 'capital', 'region', 'posts')


class PostImageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ('post', 'image')

    def validate_post(self, value):
        images = PostImage.objects.filter(post=value)
        if len(images) == 10:
            raise serializers.ValidationError(
                {'message': 'Вы можете загрузить максимум 10 фотографий.'}
            )
        return value
