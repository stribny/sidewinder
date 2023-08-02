import pytest
from openapi_spec_validator import openapi_v30_spec_validator
from rest_framework.reverse import reverse


@pytest.mark.django_db
def test_openapi_spec(client):
    response = client.get(reverse("schema") + "?format=json")

    # If no exception is raised the spec is valid
    openapi_v30_spec_validator.validate(response.json())
