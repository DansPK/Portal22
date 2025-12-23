"""
Portal22 - Phase 1.2 Schemas
Connection Management API request/response models
"""
from datetime import datetime
from typing import Optional, Literal
from pydantic import BaseModel, Field, field_validator


class ConnectionCreate(BaseModel):
    """Create new SSH connection"""
    name: str = Field(..., min_length=1, max_length=100, description="User-friendly connection name")
    description: Optional[str] = Field(None, description="Optional notes about the connection")
    host: str = Field(..., min_length=1, max_length=255, description="SSH host (IP or hostname)")
    port: int = Field(22, ge=1, le=65535, description="SSH port number")
    username: str = Field(..., min_length=1, max_length=100, description="SSH username")
    auth_method: Literal["password", "key", "key_with_passphrase"] = Field(..., description="Authentication method")
    password: Optional[str] = Field(None, description="Password (will be encrypted)")
    ssh_key_id: Optional[int] = Field(None, description="SSH key ID for key-based auth")
    color: Optional[str] = Field(None, pattern=r"^#[0-9A-Fa-f]{6}$", description="Hex color code")
    icon: Optional[str] = Field(None, max_length=50, description="Icon identifier")
    favorite: bool = Field(False, description="Mark as favorite")

    @field_validator("host")
    @classmethod
    def validate_host(cls, v: str) -> str:
        """Strip whitespace and ensure not empty"""
        v = v.strip()
        if not v:
            raise ValueError("Host cannot be empty")
        return v

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) -> str:
        """Strip whitespace from username"""
        return v.strip()

    def model_post_init(self, __context):
        """Validate auth_method matches provided credentials"""
        if self.auth_method == "password" and not self.password:
            raise ValueError("Password is required when auth_method is 'password'")
        if self.auth_method in ["key", "key_with_passphrase"] and not self.ssh_key_id:
            raise ValueError("ssh_key_id is required when auth_method is 'key' or 'key_with_passphrase'")


class ConnectionUpdate(BaseModel):
    """Update existing SSH connection (all fields optional)"""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = None
    host: Optional[str] = Field(None, min_length=1, max_length=255)
    port: Optional[int] = Field(None, ge=1, le=65535)
    username: Optional[str] = Field(None, min_length=1, max_length=100)
    auth_method: Optional[Literal["password", "key", "key_with_passphrase"]] = None
    password: Optional[str] = None
    ssh_key_id: Optional[int] = None
    color: Optional[str] = Field(None, pattern=r"^#[0-9A-Fa-f]{6}$")
    icon: Optional[str] = Field(None, max_length=50)
    favorite: Optional[bool] = None

    @field_validator("host")
    @classmethod
    def validate_host(cls, v: Optional[str]) -> Optional[str]:
        """Strip whitespace and ensure not empty if provided"""
        if v is not None:
            v = v.strip()
            if not v:
                raise ValueError("Host cannot be empty")
        return v

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: Optional[str]) -> Optional[str]:
        """Strip whitespace from username if provided"""
        if v is not None:
            v = v.strip()
        return v


class ConnectionResponse(BaseModel):
    """SSH connection information (response)"""
    id: int
    user_id: int
    name: str
    description: Optional[str]
    host: str
    port: int
    username: str
    auth_method: str
    ssh_key_id: Optional[int]
    color: Optional[str]
    icon: Optional[str]
    favorite: bool
    last_connected_at: Optional[datetime]
    connection_count: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ConnectionList(BaseModel):
    """List of SSH connections with total count"""
    connections: list[ConnectionResponse]
    total: int


class ConnectionDelete(BaseModel):
    """Connection deletion confirmation"""
    message: str
    id: int
