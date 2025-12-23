from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, Index
from sqlalchemy.orm import relationship

from app.database import Base


class Connection(Base):
    """SSH connection configuration"""
    __tablename__ = "connections"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, default=1, index=True)

    # Connection Identity
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)

    # SSH Details
    host = Column(String(255), nullable=False)
    port = Column(Integer, nullable=False, default=22)
    username = Column(String(100), nullable=False)

    # Authentication
    auth_method = Column(String(20), nullable=False)  # 'password', 'key', 'key_with_passphrase'
    password_encrypted = Column(Text, nullable=True)
    ssh_key_id = Column(Integer, ForeignKey("ssh_keys.id", ondelete="SET NULL"), nullable=True, index=True)

    # UI/UX
    color = Column(String(7), nullable=True)
    icon = Column(String(50), nullable=True)
    favorite = Column(Boolean, default=False, nullable=False, index=True)

    # Usage Tracking
    last_connected_at = Column(DateTime, nullable=True, index=True)
    connection_count = Column(Integer, default=0, nullable=False)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="connections")
    ssh_key = relationship("SSHKey", back_populates="connections")
    sessions = relationship("SSHSession", back_populates="connection", cascade="all, delete-orphan")

    # Composite unique constraint: user cannot have duplicate connection names
    __table_args__ = (
        Index('ix_user_connection_name', 'user_id', 'name', unique=True),
    )
