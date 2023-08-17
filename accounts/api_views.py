from django.contrib.auth import get_user_model
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.serializers import ImsRegisterSerializer, ImsUserSerializer, ImsTokenObtainPairSerializer

UserModel = get_user_model()


class ImsTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = ImsTokenObtainPairSerializer


class ImsRegisterApi(CreateAPIView):
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ImsRegisterSerializer


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        user = UserModel.objects.get(id=request.user.id)
        serializer = ImsUserSerializer(user)
        return Response(serializer.data)
