import pytest
from django.core.urlresolvers import reverse
from rest_framework.test import APIClient

API_VERSION = '1.0'


@pytest.mark.django_db(transaction=True)
def test_root_get():
    client = APIClient()
    url = reverse('rest_api:root', kwargs=dict(version=API_VERSION))
    assert url == '/api/1.0/'
    response = client.get(url)
    assert response.status_code == 403
