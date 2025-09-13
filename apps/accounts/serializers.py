from typing import Any

from django.contrib.auth import authenticate
from rest_framework import serializers, status
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, max_length=30)
    password2 = serializers.CharField(write_only=True, max_length=30)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def create(self, validated_data):
        password = validated_data.pop('password1')
        validated_data.pop('password2')
        validated_data['password'] = password
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def to_representation(self, instance):
        data = {
            "user_id": instance.id,
            "username": instance.username
        }
        return data


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Username yoki parol xato")
        attrs['user'] = user
        return attrs


class RefreshTokenSerializer(TokenRefreshSerializer):
    def validate(self, attrs: dict[str, Any]):
        user_token = attrs.get('refresh')
        if not user_token:
            raise serializers.ValidationError({"error": "Reresh token kiritish majburiy"})

        refresh = RefreshToken(user_token)
        access_token = refresh.access_token

        user_id = refresh["user_id"]
        user = User.objects.get(id=user_id)

        return {
            "access": str(access_token),
            "user_id": user.id,
            "username": user.username,
            "email": user.email
        }
