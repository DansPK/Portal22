"""
Portal22 - Phase 1.4 Database Models
SSH Session Tracking and History
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Index
from sqlalchemy.orm import relationship

from app.database import Base


class SSHSession(Base):
    """SSH connection session tracking and history"""
    __tablename__ = "ssh_sessions"

    # Primary key
    id = Column(Integer, primary_key=True, index=True)
    connection_id = Column(Integer, ForeignKey("connections.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, default=1, index=True)

    # Session Identity
    session_uuid = Column(String(36), unique=True, nullable=False, index=True)  # UUID for WebSocket routing

    # Session State
    status = Column(String(20), nullable=False, default="connecting", index=True)
    # Values: 'connecting', 'active', 'closed', 'failed'

    # Connection Details
    server_ip = Column(String(45), nullable=True)  # Resolved IP address (IPv6 support)

    # Timing
    started_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    ended_at = Column(DateTime, nullable=True)
    duration_seconds = Column(Integer, nullable=True)  # Calculated when session closes

    # Terminal Info
    terminal_rows = Column(Integer, default=24, nullable=False)  # Terminal height
    terminal_cols = Column(Integer, default=80, nullable=False)  # Terminal width

    # Error Handling
    error_message = Column(Text, nullable=True)  # Error details if status='failed'
    disconnection_reason = Column(String(50), nullable=True)
    # Values: 'user_closed', 'timeout', 'error', 'server_closed', 'network_error'

    # Relationships
    connection = relationship("Connection", back_populates="sessions")
    user = relationship("User", back_populates="ssh_sessions")
