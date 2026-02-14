"""Tests for the /search endpoint."""

from fastapi.testclient import TestClient

from app.main import app
from app.store import profile_store

client = TestClient(app)


def test_search_with_query(clean_store):
    profile_store["alice"] = {"username": "alice", "bio": "dev"}
    profile_store["alex"] = {"username": "alex", "bio": "designer"}
    profile_store["bob"] = {"username": "bob", "bio": "manager"}

    response = client.get("/search?q=al")
    data = response.json()

    assert data["total"] == 2
    assert len(data["results"]) == 2


def test_search_empty_query(clean_store):
    profile_store["carol"] = {"username": "carol", "bio": "tester"}

    response = client.get("/search?q=")
    data = response.json()

    assert data["total"] > 0
