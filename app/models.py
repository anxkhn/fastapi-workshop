"""Data models for the Workshop API."""

from pydantic import BaseModel
from typing import Optional


class ProfileCreate(BaseModel):
    """Schema for creating a new profile."""

    username: str
    bio: str
    age: Optional[int] = None


class ProfileResponse(BaseModel):
    """Schema for profile responses."""

    username: str
    name: Optional[str] = None
    bio: str
    age: Optional[int] = None
