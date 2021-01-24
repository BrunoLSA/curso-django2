import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def response(client, modulo):
    response = client.get(reverse("modulos:detalhe", kwargs={'slug': modulo.slug}))
    return response


def test_titulo(response, modulo: Modulo):
    assert_contains(response, modulo.titulo)


def test_descricao(response, modulo: Modulo):
    assert_contains(response, modulo.descricao)


def test_publico(response, modulo: Modulo):
    assert_contains(response, modulo.publico)
