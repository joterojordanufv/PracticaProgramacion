from uuid import uuid4
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def unique_email(prefix="integration"):
    return f"{prefix}_{uuid4().hex}@test.com"


def test_get_books():
    response = client.get("/books/")

    assert response.status_code == 200


def test_create_user():
    response = client.post(
        "/users/",
        json={
            "nombre": "Usuario Test Integracion",
            "email": unique_email()
        }
    )

    assert response.status_code == 200
