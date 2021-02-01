from typing import List

import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulos(db):
    return baker.make(Modulo, 2)


@pytest.fixture
def aulas(modulos):
    aulas = []
    for modulo in modulos:
        aula = baker.make(Aula, 3, modulo=modulo)
        aulas.extend(aula)
    return aulas


@pytest.fixture
def response(client, modulos, aulas):
    response = client.get(reverse("modulos:indice"))
    return response


def test_indice_disponivel(response):
    assert response.status_code == 200


def test_titulo(response, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(response, modulo.titulo)


def test_descricao(response, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(response, modulo.descricao)


def test_publico(response, modulos: List[Modulo]):
    for modulo in modulos:
        assert_contains(response, modulo.publico)


def test_aula_titulo(response, aulas: List[Aula]):
    for aula in aulas:
        assert_contains(response, aula.titulo)


def test_aula_link(response, aulas):
    for aula in aulas:
        assert_contains(response, aula.get_absolute_url())
