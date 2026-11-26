# STEP 1: pytest discovers test functions in this file automatically.
import pytest

# STEP 2: Import the factory instead of the global app to keep tests isolated.
from app import create_app


# STEP 3: A fixture builds a fresh test client for every test function.
@pytest.fixture
def client():
    # STEP 3.1: create_app compiles FSCSS once more; that is cheap and safe here.
    app = create_app()

    # STEP 3.2: TESTING mode surfaces errors instead of hiding them in responses.
    app.config.update(TESTING=True)

    # STEP 3.3: Flask's test client can call routes without starting a server.
    return app.test_client()


# STEP 4: Smoke test the landing page and its premium frontend hooks.
def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"AutoStore" in response.data
    assert b"Sell what you have" in response.data
    assert b"cdn.tailwindcss.com" not in response.data
    assert b"/style.css" in response.data
    assert b"/main.js" in response.data
    assert b"motion@12.23.24" in response.data
    assert b"Playfair+Display" in response.data
    assert b"data-parallax" in response.data
    assert b"premium-card" in response.data
    assert b"og:title" in response.data
    assert b"og-image.png" in response.data
    assert b"twitter:card" in response.data
    assert b"favicon.svg" in response.data
    assert b"rel=\"canonical\"" in response.data


# STEP 5: Smoke test the second page to prove url_for links have a target.
def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"Our vision" in response.data
    assert b"About AutoStore" in response.data
    assert b"og-about.png" in response.data


# STEP 6: Verify the JSON health endpoint returns the exact expected payload.
def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "service": "AutoStore"}


# STEP 7: Verify the custom 404 template is used and keeps status code 404.
def test_404(client):
    response = client.get("/missing")
    assert response.status_code == 404
    assert b"off the map" in response.data


# STEP 8: Social previews need real, reachable assets at stable public URLs.
@pytest.mark.parametrize(
    ("path", "signature"),
    [
        ("/og-image.png", b"\x89PNG"),
        ("/og-about.png", b"\x89PNG"),
        ("/favicon.svg", b"<svg"),
    ],
)
def test_social_assets(client, path, signature):
    response = client.get(path)
    assert response.status_code == 200
    assert signature in response.data[:32]
