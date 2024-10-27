from rest_framework import serializers

from posts.models import Country, Tag, Post, PostImage, Comment


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

    def validate_user(self, value):
        if not value.can_post:
            raise serializers.ValidationError(
                {'message': 'У вас нет разрешения на создание поста.'}
            )
        return value


class PostSerializer(serializers.ModelSerializer):
    tag = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Post
        fields = ('id', 'topic', 'description', 'tag')


class CountryDetailSerializer(serializers.ModelSerializer):
    posts = PostSerializer(source='country_posts', many=True, read_only=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'alpha2Code', 'alpha3Code', 'capital', 'region', 'posts')


class PostImageCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = ('post', 'image')

    def validate(self, attrs):
        post=attrs.get('post')
        images = PostImage.objects.filter(post=post)
        if len(images) == 10:
            raise serializers.ValidationError(
                {'message': 'Вы можете загрузить максимум 10 фотографий.'}
            )
        user = self.context['request'].user
        if not user.can_post:
            raise serializers.ValidationError(
                {'message': 'У вас нет разрешения на создание поста.'}
            )
        return attrs


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('post', 'text')


class PostDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    tag = TagListCreateSerializer(read_only=True, many=True)
    post_images = PostImageSerializer(many=True, read_only=True)
    comments = CommentCreateSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'topic', 'description', 'country', 'tag', 'post_images', 'comments')
