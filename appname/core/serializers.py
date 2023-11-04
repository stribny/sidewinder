from rest_framework import serializers


class GetTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class TokenSerializer(serializers.Serializer):
    token = serializers.CharField()


class ProtectedViewSerializer(serializers.Serializer):
    message = serializers.CharField()
