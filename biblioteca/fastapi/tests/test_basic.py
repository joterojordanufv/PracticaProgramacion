from uuid import uuid4
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def unique_email(prefix="test"):
    return f"{prefix}_{uuid4().hex}@test.com"


def test_create_book():
    response = client.post("/books/", json={
        "titulo": "Test Book",
        "autor": "Test Author",
        "genero": "Test"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "Test Book"


def test_create_user():
    response = client.post("/users/", json={
        "nombre": "Pepe",
        "email": unique_email("pepe")
    })

    assert response.status_code == 200
    data = response.json()
    assert data["nombre"] == "Pepe"


def test_duplicate_user():
    email = unique_email("duplicate")

    first_response = client.post("/users/", json={
        "nombre": "Pepe",
        "email": email
    })

    assert first_response.status_code == 200

    second_response = client.post("/users/", json={
        "nombre": "Otro",
        "email": email
    })

    assert second_response.status_code == 400


def test_create_loan():
    book_response = client.post("/books/", json={
        "titulo": "Loan Book",
        "autor": "Autor",
        "genero": "Test"
    })

    assert book_response.status_code == 200
    book = book_response.json()

    user_response = client.post("/users/", json={
        "nombre": "User Loan",
        "email": unique_email("loan")
    })

    assert user_response.status_code == 200
    user = user_response.json()

    loan_response = client.post("/loans/", json={
        "user_id": user["id"],
        "book_id": book["id"]
    })

    assert loan_response.status_code == 200
