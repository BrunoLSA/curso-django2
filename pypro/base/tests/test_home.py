import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def response(client, db):
    response = client.get(reverse("base:home"))
    return response


def test_status_code(response):
    assert response.status_code == 200


def test_title(response):
    assert_contains(response, '<title>Python Pro - Home</title>')


def test_home_link(response):
    assert_contains(response, f'href="{reverse("base:home")}">Python Pro</a>')


def test_email_link(response):
    assert_contains(response, 'href="mailto:ramalho@python.pro.br"')
