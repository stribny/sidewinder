import pytest
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch


def test_login_as_user_not_available_ifnot_debug(client):
    with pytest.raises(NoReverseMatch):
        client.post(reverse("login_as_user"), {"select_user": "1"})
