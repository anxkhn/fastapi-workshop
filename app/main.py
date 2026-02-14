"""Workshop API - a tiny FastAPI application for open-source contribution practice."""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from app.models import ProfileCreate, ProfileResponse
from app.store import profile_store


app = FastAPI(title="FastAPI Workshop", version="0.1.0")


# Enable CORS for all origins (useful for frontend testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# =========================
# Health Endpoint
# =========================

@app.get("/health", status_code=200)
def health_check():
    """Return the health status of the API."""
    return {"status": "ok"}


# =========================
# Sum Endpoint (Fixed bug)
# =========================

@app.get("/sum")
def compute_sum(a: int = Query(...), b: int = Query(...)):
    """Return the sum of two integers."""
    return {"result": a + b}


# =========================
# Helper function
# =========================

def format_profile(data: dict):
    """Format profile response consistently."""
    return {
        "username": data["username"],
        "name": data["username"],
        "bio": data["bio"],
        "age": data.get("age"),
    }


# =========================
# Profile Endpoints
# =========================

@app.post("/profile", status_code=201)
def create_profile(profile: ProfileCreate):
    """Create a new user profile."""
    profile_store[profile.username] = {
        "username": profile.username,
        "bio": profile.bio,
        "age": profile.age,
    }

    return format_profile(profile_store[profile.username])


@app.get("/profile/{username}")
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


# =========================
# Search Endpoint (Fully fixed)
# =========================

@app.get("/search")
def search_profiles(
    q: str = Query(default=""),
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1),
):
    """
    Search profiles by username or bio.

    - Empty query returns all profiles
    - Correct pagination slicing
    - total field reflects full result count
    """

    # If query empty → return all profiles
    if q == "":
        filtered_results = list(profile_store.values())
    else:
        filtered_results = [
            profile
            for profile in profile_store.values()
            if q.lower() in profile["username"].lower()
            or q.lower() in profile["bio"].lower()
        ]

    total_count = len(filtered_results)

    # Correct pagination slicing
    paginated_results = filtered_results[offset : offset + limit]

    # Format output consistently
    formatted_results = [format_profile(profile) for profile in paginated_results]

    return {
        "results": formatted_results,
        "total": total_count,
    }
