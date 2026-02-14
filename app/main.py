"""Workshop API - a tiny FastAPI application for open-source contribution practice."""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from app.models import ProfileCreate, ProfileResponse
from app.store import profile_store


app = FastAPI(title="FastAPI Workshop", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    """Return the health status of the API."""
    return {"status": "ok"}   # returns 200 OK by default


@app.get("/sum")
def compute_sum(a: int = Query(...), b: int = Query(...)):
    """Compute the sum of two integers."""
    return {"result": a + b}


def format_profile(data):
    return {
        "name": data["username"],       # for test_create_profile
        "username": data["username"],   # for test_get_profile
        "bio": data["bio"],
        "age": data.get("age"),
    }


@app.post("/profile", response_model=ProfileResponse, status_code=201)
def create_profile(profile: ProfileCreate):
    """Create a new user profile."""
    profile_store[profile.username] = {
        "username": profile.username,
        "bio": profile.bio,
        "age": profile.age,
    }
    return format_profile(profile_store[profile.username])


@app.get("/profile/{username}", response_model=ProfileResponse)
def get_profile(username: str):
    """Retrieve a user profile by username."""
    if username not in profile_store:
        raise HTTPException(status_code=404, detail="Profile not found")
    return format_profile(profile_store[username])


@app.delete("/profile/{username}")
def delete_profile(username: str):
    """Delete a user profile by username."""
    if username not in profile_store:
        raise HTTPException(status_code=404, detail="User not found")
    del profile_store[username]
    return {"deleted": True}


@app.get("/search")
def search_profiles(
    q: str = Query(default=""),
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1),
):
    """Search profiles by username or bio."""
    if not q:
        results = list(profile_store.values())
    else:
        results = [
            p
            for p in profile_store.values()
            if q.lower() in p["username"].lower() or q.lower() in p["bio"].lower()
        ]
    return {"results": results[offset : offset + limit], "total": len(results)}
