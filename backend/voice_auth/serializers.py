from rest_framework import serializers
from .models import User, Voiceprint

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class VoiceprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voiceprint
        fields = ('id', 'user', 'voice_data')

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField()
    voice_data = serializers.CharField()

    def create(self, validated_data):
        # This is where you would process the voice data and create the user and voiceprint
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        voice_data = validated_data['voice_data']

        user = User.objects.create_user(username=username, password=password, email=email)
        # Note: You will replace this part with your actual voiceprint creation logic
        # For now, we are just saving the raw data.
        Voiceprint.objects.create(user=user, voice_data=voice_data.encode())
        
        return user