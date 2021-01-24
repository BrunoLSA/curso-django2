import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def response(client, modulos):
    response = client.get(reverse("base:home"))
    return response


def test_email_link(response, modulos):
    for modulo in modulos:
        assert_contains(response, modulo.titulo)
