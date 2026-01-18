from rest_framework import serializers

from packages.kernel.adapters import ModelSerializerAdapter


class LoginSerializer(ModelSerializerAdapter):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, min_length=8, max_length=100)


class RegisterSerializer(ModelSerializerAdapter):
    name = serializers.CharField(required=True)
    inn = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    surname = serializers.CharField(required=True)
    position = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    role = serializers.IntegerField(required=True)
