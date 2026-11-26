import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"FSCSS" in response.data


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Project layout" in response.data


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "service": "Flask + FSCSS boilerplate"}


def test_404(client):
    response = client.get("/missing")
    assert response.status_code == 404
    assert b"off the map" in response.data
