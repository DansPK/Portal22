from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, LargeBinary, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # Phase 1.1: username max 50 chars (kept unique + indexed)
    username = Column(String(50), unique=True, index=True, nullable=False)

    # Legacy field kept for backward compatibility with existing code/tests
    hashed_password = Column(String(255), nullable=False)

    # Phase 1.1: Argon2id master password hash + 32-byte salt for key derivation
    master_password_hash = Column(String(255), nullable=True)
    salt = Column(LargeBinary(32), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    last_login_at = Column(DateTime, nullable=True)

    sessions = relationship(
        "UserSession", back_populates="user", cascade="all, delete-orphan"
    )


class UserSession(Base):
    __tablename__ = "user_sessions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)

    # Legacy field kept for compatibility with current auth flow
    token = Column(String(128), unique=True, index=True, nullable=True)

    # Phase 1.1: canonical session token field
    session_token = Column(String(255), unique=True, index=True, nullable=True)

    ip_address = Column(String(45), nullable=True)
    user_agent = Column(Text, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    expires_at = Column(DateTime, index=True, nullable=True)
    last_activity_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    user = relationship("User", back_populates="sessions")
