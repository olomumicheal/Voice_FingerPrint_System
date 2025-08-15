from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Voiceprint
from .serializers import UserSerializer, VoiceprintSerializer
import json

class RegisterView(APIView):
    """
    Handles user registration.
    """
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            # We are not doing complex voiceprint analysis yet, just saving the data.
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
            voice_data = data.get('voice_data')

            if not username or not email or not password or not voice_data:
                return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

            # Check if username or email already exists
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return Response({"error": "Username or email already exists."}, status=status.HTTP_409_CONFLICT)

            # Create the user and voiceprint
            user = User.objects.create_user(username=username, email=email, password=password)
            voiceprint = Voiceprint.objects.create(user=user, data=voice_data)

            return Response({
                "message": "Registration successful. You can now log in.",
                "user_id": user.id,
                "voiceprint_id": voiceprint.id
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LoginView(APIView):
    """
    Handles user login.
    """
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            # For this temporary logic, we'll just check if the user exists.
            # In a real system, you would compare the new voice data against the stored voiceprint.
            username = data.get('username')
            # You can also use other data sent from frontend, e.g., voice_data
            
            if not username:
                 return Response({"error": "Username is required for login."}, status=status.HTTP_400_BAD_REQUEST)

            if User.objects.filter(username=username).exists():
                # This is the "success" response that the frontend will look for.
                return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


