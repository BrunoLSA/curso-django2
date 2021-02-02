import pytest
from django.urls import reverse
from model_bakery import baker

from pypro.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def response(client, db):
    return client.get(reverse('login'))


def test_login_form_page(response):
    assert response.status_code == 200


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = baker.make(django_user_model)
    senha = 'senha'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def response_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.email, 'password': usuario.senha_plana})


def test_login_redirect(response_post):
    assert response_post.status_code == 302
    assert response_post.url == reverse('modulos:indice')


@pytest.fixture
def response_home(client, db):
    return client.get(reverse('base:home'))


def test_botao_entrar_disponivel(response_home):
    assert_contains(response_home, 'Entrar')


def test_link_login_disponivel(response_home):
    assert_contains(response_home, reverse('login'))


@pytest.fixture
def response_home_com_usuario_logado(client_com_usuario_logado, db):
    return client_com_usuario_logado.get(reverse('base:home'))


def test_botao_entrar_indisponivel(response_home_com_usuario_logado):
    assert_not_contains(response_home_com_usuario_logado, 'Entrar')


def test_link_login_indisponivel(response_home_com_usuario_logado):
    assert_not_contains(response_home_com_usuario_logado, reverse('login'))


def test_botao_sair_disponivel(response_home_com_usuario_logado):
    assert_contains(response_home_com_usuario_logado, 'Sair')


def test_nome_usuario_logado_disponivel(response_home_com_usuario_logado, usuario_logado):
    assert_contains(response_home_com_usuario_logado, usuario_logado.first_name)


def test_link_logout_disponivel(response_home_com_usuario_logado):
    assert_contains(response_home_com_usuario_logado, reverse('logout'))
