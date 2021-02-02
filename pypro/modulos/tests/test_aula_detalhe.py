import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def response(client_com_usuario_logado, aula):
    response = client_com_usuario_logado.get(reverse("modulos:aula", kwargs={'slug': aula.slug}))
    return response


def test_titulo(response, aula: Aula):
    assert_contains(response, aula.titulo)


def test_vimeo(response, aula: Aula):
    assert_contains(response, f'https://player.vimeo.com/video/{ aula.vimeo_id }')


def test_modulo_breadcrumb(response, modulo: Modulo):
    assert_contains(response, f'class="breadcrumb-item"><a href="{modulo.get_absolute_url()}">{modulo.titulo}')


@pytest.fixture
def response_sem_usuario(client, aula):
    response = client.get(reverse("modulos:aula", kwargs={'slug': aula.slug}))
    return response


def test_usuario_nao_logado_redirect(response_sem_usuario):
    assert response_sem_usuario.status_code == 302
    assert response_sem_usuario.url.startswith(reverse('login'))
