import os

import pytest
from rest_framework.test import APIClient

from .core.fixtures.factories import *  # noqa

os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


@pytest.fixture()
def client():
    return APIClient()
