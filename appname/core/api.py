from allauth.account.auth_backends import AuthenticationBackend
from drf_spectacular.utils import extend_schema
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


class AuthTokenView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request=serializers.GetTokenSerializer,
        responses=serializers.TokenSerializer,
    )
    def post(self, request):
        """
        Returns a user's API token given correct
        credentials.
        """

        serializer = serializers.GetTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = AuthenticationBackend().authenticate(
            request, **serializer.validated_data
        )
        if not user:
            raise AuthenticationFailed()
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
            }
        )


class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ProtectedViewSerializer

    def get(self, request):
        context = {"message": "Hello, World!"}
        return Response(context)
