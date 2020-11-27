from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework_simplejwt import authentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import NetBoxUser
from .serializers import NetBoxUserSerializer, NetBoxTokenObtainPairSerializer

class NetBoxUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = NetBoxUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NetBoxTokenObtainPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = NetBoxTokenObtainPairSerializer

class AuthTest(APIView):
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.JWTAuthentication, )

    def get(self, request):
        return Response(None, status=status.HTTP_200_OK)
