from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, Voiceprint
from .serializers import UserRegistrationSerializer
import json
import base64
import binascii # We need to import the specific library for the error type

def compare_voice_data(data1, data2):
    """
    Compares two Base64 strings and returns a similarity score.
    This version includes more specific error handling.
    """
    if not data1 or not data2:
        return 0.0, "Missing data." # Return a descriptive message

    # Decode the Base64 strings with specific error handling
    try:
        bytes1 = base64.b64decode(data1)
        bytes2 = base64.b64decode(data2)
    except binascii.Error as e:
        # If Base64 decoding fails, we know the exact cause.
        print(f"Base64 decoding error: {e}")
        return 0.0, f"Base64 decoding failed: {e}"
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected decoding error: {e}")
        return 0.0, f"An unexpected error occurred: {e}"

    # Calculate similarity based on a simple byte-by-byte comparison.
    min_len = min(len(bytes1), len(bytes2))
    matching_bytes = 0
    for i in range(min_len):
        if bytes1[i] == bytes2[i]:
            matching_bytes += 1
    
    # Calculate a similarity percentage
    max_len = max(len(bytes1), len(bytes2))
    if max_len == 0:
        return 0.0, "Zero-length data."
    
    return (matching_bytes / max_len), "Success"

class RegisterView(APIView):
    # (The RegisterView is unchanged, as the error was in the Login process)
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                username = serializer.validated_data['username']
                voice_data = serializer.validated_data['voice_data']

                # Create the user and voiceprint
                user = User.objects.create_user(
                    username=username,
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password']
                )
                Voiceprint.objects.create(user=user, data=voice_data)

                return Response({
                    "message": "Registration successful. You can now log in."
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                # Log the specific error for debugging
                print(f"Registration Error: {e}")
                return Response({"error": "An internal server error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    Handles user login using a simple voice data comparison.
    """
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        voice_data = request.data.get("voice_data")

        if not username or not voice_data:
            return Response({"error": "Username and voice data are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        
        try:
            stored_voiceprint = Voiceprint.objects.get(user=user)
        except Voiceprint.DoesNotExist:
            return Response({"error": "No voiceprint found for this user."},
                            status=status.HTTP_404_NOT_FOUND)
        
        # Call the new voice comparison function
        similarity_score, error_message = compare_voice_data(stored_voiceprint.data, voice_data)
        
        SUCCESS_THRESHOLD = 0.70 

        if error_message != "Success":
            # If the voice data itself is the problem, return a 400 Bad Request
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)

        if similarity_score >= SUCCESS_THRESHOLD:
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid voice data. Similarity score: {:.2f}%".format(similarity_score * 100)}, 
                            status=status.HTTP_401_UNAUTHORIZED)
