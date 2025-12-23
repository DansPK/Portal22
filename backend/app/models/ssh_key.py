"""
Portal22 - Phase 1.3 Database Models
SSH Key Storage and Management
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Index
from sqlalchemy.orm import relationship

from app.database import Base


class SSHKey(Base):
    """SSH key pair storage with encryption"""
    __tablename__ = "ssh_keys"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, default=1, index=True)

    # Key Identity
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)

    # Key Details
    key_type = Column(String(20), nullable=False)  # 'rsa', 'ed25519', 'ecdsa', 'dsa'
    key_size = Column(Integer, nullable=True)  # 2048, 4096 for RSA, 256/384/521 for ECDSA, NULL for ed25519

    # Key Data (encrypted)
    public_key = Column(Text, nullable=False)  # Plain text SSH public key (ssh-rsa, ssh-ed25519, etc.)
    private_key_encrypted = Column(Text, nullable=False)  # AES-256-GCM encrypted private key (base64)
    passphrase_encrypted = Column(Text, nullable=True)  # Encrypted passphrase if key has one

    # Metadata
    fingerprint = Column(String(100), nullable=True, index=True)  # SHA256 fingerprint for verification
    comment = Column(Text, nullable=True)  # Comment from key file (email or description)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    user = relationship("User", back_populates="ssh_keys")
    connections = relationship("Connection", back_populates="ssh_key")

    # Composite unique constraint: user cannot have duplicate key names
    __table_args__ = (
        Index('ix_user_key_name', 'user_id', 'name', unique=True),
    )
