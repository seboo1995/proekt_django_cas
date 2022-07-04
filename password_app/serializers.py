from dataclasses import field
from rest_framework.serializers import ModelSerializer
from .models import Password
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PasswordSerializer(ModelSerializer):
    class Meta:
        model = Password
        fields = '__all__'
        def create(self,validated_data):
            return Password.objects.create(**validated_data)
