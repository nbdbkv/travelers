from django.db.models import Count
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.models import CustomUser
from accounts.serializers import (
    UserListSerializer, UserRegisterSerializer, UserVerifySerializer, ProfileSerializer, ProfileUpdateSerializer,
    TokenAccessSerializer,
)


class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = CustomUser.objects.annotate(
            post_count=Count('user_posts'),
            country_count=Count('user_posts__country', distinct=True)
        )
        return queryset


class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)


class UserVerifyView(generics.GenericAPIView):
    serializer_class = UserVerifySerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.update()
        tokens = user.tokens()
        return Response(tokens, status=status.HTTP_202_ACCEPTED)


class ProfileView(generics.RetrieveAPIView):
    queryset = CustomUser
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ProfileUpdateView(generics.UpdateAPIView):
    queryset = CustomUser
    serializer_class = ProfileUpdateSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class TokenAccessView(TokenObtainPairView):
    serializer_class = TokenAccessSerializer
