import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.core.fixtures.defaults import DEFAULT_PASSWORD


@pytest.mark.django_db
def test_auth_token_view(client, user_factory):
    """
    User can obtain a valid token by providing correct
    email and password.
    """

    user = user_factory()

    response = client.post(
        reverse("token_auth"), {"email": user.email, "password": DEFAULT_PASSWORD}
    )

    assert response.status_code == status.HTTP_200_OK
    assert "token" in response.json()


@pytest.mark.django_db
def test_auth_token_view_invalid_password(client, user_factory):
    """
    Token is not returned when bad password is provided.
    """

    user = user_factory()

    response = client.post(
        reverse("token_auth"), {"email": user.email, "password": "invalid password"}
    )

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert "token" not in response.json()


@pytest.mark.django_db
def test_protected_view_not_accessible(client):
    """
    View with [IsAuthenticated] can't be accessed without a valid
    token.
    """

    response = client.get(reverse("protected"))

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_protected_view_access_with_token(client, token_factory):
    """
    View with [IsAuthenticated] can be accessed with a valid
    token.
    """

    token = token_factory()
    client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

    response = client.get(reverse("protected"))

    assert response.status_code == status.HTTP_200_OK
