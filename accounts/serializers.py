from django.core.cache import cache
from django.utils import timezone

from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from accounts.choices import OTPType
from accounts.models import CustomUser
from accounts.services import send_otp_to_email
from posts.serializers import PostSerializer


class UserListSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    country_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'post_count', 'country_count')

    def get_post_count(self, obj):
        return getattr(obj, 'post_count', 0)

    def get_country_count(self, obj):
        return getattr(obj, 'country_count', 0)


class UserDetailSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'user_posts')


class UserRegisterSerializer(serializers.ModelSerializer):
    otp_type = serializers.IntegerField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'otp_type')

    def validate(self, attrs):
        email = attrs['email']
        otp_type = attrs['otp_type']
        user = CustomUser.objects.filter(email=email).exists()
        if user and (otp_type == OTPType.REGISTER):
            raise serializers.ValidationError(
                {'message': 'Пользователь с такой электронной почтой уже существует.'}
            )
        elif not user and (otp_type == OTPType.RESET_PASSWORD):
            raise serializers.ValidationError(
                {'message': 'Пользователь с такой электронной почтой не существует.'}
            )
        return attrs

    def create(self, validated_data):
        email = validated_data.get('email')
        otp_type = validated_data.get('otp_type')
        user = CustomUser.objects.create(email=email)
        send_otp_to_email(email, otp_type)
        return user


class UserVerifySerializer(serializers.Serializer):
    otp = serializers.IntegerField(required=True)

    def validate_otp(self, value):
        email = cache.get(value, version=OTPType.REGISTER)
        if email is not None:
            self.instance = CustomUser.objects.get(email=email)
            return value
        raise ValidationError('Неправильный код ОТП.')

    def update(self):
        self.instance.is_active = True
        self.instance.verify_date = timezone.now()
        self.instance.save()
        return self.instance


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class ProfileUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'password')

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class TokenAccessSerializer(TokenObtainPairSerializer):

    default_error_messages = {'no_active_account': 'Неверная электронная почта или пароль.'}

    def validate(self, attrs):
        data = super().validate(attrs)
        if not self.user.has_access:
            raise AuthenticationFailed('У вас нет доступа к системе.')
        return data
