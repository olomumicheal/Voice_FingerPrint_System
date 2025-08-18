from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Voiceprint

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    It includes password and voice data fields for creation.
    """
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    voice_data = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'voice_data')

    def create(self, validated_data):
        """
        Custom create method to handle user and voiceprint creation.
        Note: This method is not used by the RegisterView I provided.
        The view handles creation directly after validation.
        This is here for completeness.
        """
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        email = validated_data.pop('email')
        voice_data = validated_data.pop('voice_data')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            **validated_data
        )
        Voiceprint.objects.create(user=user, data=voice_data)
        
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login validation.
    """
    username = serializers.CharField(required=True)
    voice_data = serializers.CharField(required=True)
