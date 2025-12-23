"""
Portal22 - Models Package
Import all database models for easy access

Phase 1.1: User authentication
Phase 1.2: Connection management
Phase 1.3: SSH key management
Phase 1.4: Session tracking

Usage:
    from app.models import User, UserSession, Connection, SSHKey, SSHSession

Database Relationships:
    ┌─────────────┐
    │    User     │
    │  (Phase 1.1)│
    └──────┬──────┘
           │
           │ 1:N (one user has many...)
           │
           ├───────────────┬────────────────┬────────────────┐
           │               │                │                │
           ▼               ▼                ▼                ▼
    ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
    │UserSession  │ │ Connection  │ │   SSHKey    │ │ SSHSession  │
    │ (Phase 1.1) │ │ (Phase 1.2) │ │ (Phase 1.3) │ │ (Phase 1.4) │
    └─────────────┘ └──────┬──────┘ └──────┬──────┘ └─────────────┘
                           │               │
                           │ N:1           │ 1:N
                           └───────────────┘
                        (connection uses key)
                        
                    ┌──────┴──────┐
                    │             │
                    │ 1:N         │
                    │             │
                    ▼             │
             ┌─────────────┐     │
             │ SSHSession  │◄────┘
             │ (Phase 1.4) │
             └─────────────┘
        (connection has sessions)
"""

from app.models.user import User, UserSession
from app.models.connection import Connection
from app.models.ssh_key import SSHKey
from app.models.ssh_session import SSHSession

__all__ = [
    "User",
    "UserSession",
    "Connection",
    "SSHKey",
    "SSHSession",
]
