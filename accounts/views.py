from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from accounts.models import CustomUser
from accounts.serializers import UserRegisterSerializer, UserVerifySerializer


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
