"""Data models for the Workshop API."""

from pydantic import BaseModel, Field
from typing import Optional


class ProfileCreate(BaseModel):
    """Schema for creating a new profile."""

    username: str
    bio: str = Field(..., max_length=300)
    age: Optional[int] = None


class ProfileResponse(BaseModel):
    """Schema for profile responses."""

    username: str
    bio: str
    age: Optional[int] = None
