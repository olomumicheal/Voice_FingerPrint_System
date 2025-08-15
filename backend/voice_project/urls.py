from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('voice_auth.urls')), # This line includes the URLs from your app
]
