from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginSerializer


class UserLoginView(APIView):
    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={200: UserSerializer},
        operation_summary="User Login",
        operation_description="Authenticate user and get access token"
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request=request,
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password'],
        )

        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response(
            {
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            },
            status=status.HTTP_200_OK,
        )


class UserSignupView(APIView):
    @swagger_auto_schema(
        request_body=UserSerializer,
        responses={201: UserSerializer},
        operation_summary="User Signup",
        operation_description="Create a new user account"
    )
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
