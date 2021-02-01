import pytest
from django.urls import reverse


@pytest.fixture
def response(client, db):
    return client.get(reverse('turmas:indice'))


def test_status_code(response):
    assert response.status_code == 200
