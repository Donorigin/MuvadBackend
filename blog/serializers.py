from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


# Optional: Serialize user info
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']