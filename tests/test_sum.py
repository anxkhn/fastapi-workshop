"""Tests for the /sum endpoint."""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_sum_positive_numbers():
    response = client.get("/sum?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

def test_sum_negative_numbers():
    response = client.get("/sum?a=-1&b=-4")
    assert response.status_code == 200
    assert response.json() == {"result": -5}


def test_sum_zero():
    response = client.get("/sum?a=0&b=0")
    assert response.status_code == 200
    assert response.json() == {"result": 0}
