from django.contrib.auth.models import Permission
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, UserSettingsSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import NewUser


class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserSettings(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logged_in_user = request.user
        serializer = UserSettingsSerializer(logged_in_user)
        return Response(serializer.data)

    def post(self, request, format='json'):
        serializer = UserSettingsSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            user_to_update = NewUser.objects.get(email=data['email'])
            user_to_update.opt_in = data['opt_in']
            user_to_update.save()
            return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        