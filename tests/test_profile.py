"""Tests for the /profile endpoints."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_profile(clean_store):
    response = client.post(
        "/profile",
        json={"username": "alice", "bio": "Backend developer", "age": 22},
    )
    assert response.status_code == 201
    assert response.json()["username"] == "alice"


def test_get_profile(clean_store):
    client.post(
        "/profile",
        json={"username": "bob", "bio": "Frontend developer", "age": 25},
    )
    response = client.get("/profile/bob")
    assert response.status_code == 200
    assert response.json()["username"] == "bob"


def test_get_nonexistent_profile(clean_store):
    response = client.get("/profile/nobody")
    assert response.status_code == 404
