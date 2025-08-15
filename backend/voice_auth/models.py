# backend/voice_auth/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # This is a custom user model for our project
    pass

class Voiceprint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.TextField() # Ensure this is a TextField to handle large data
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Voiceprint for {self.user.username}"