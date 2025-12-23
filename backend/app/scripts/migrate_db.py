"""
Database migration script to create Phase 1.2 tables
"""
from app.database import Base, engine
from app.models import User, UserSession, Connection, SSHKey, SSHSession


def main():
    print("Running database migration...")
    print("Creating tables for Phase 1.2 (SSH Connection Management)...")
    
    # Create all tables defined in the models
    Base.metadata.create_all(bind=engine)
    
    print("✓ Migration completed successfully!")
    print("Tables created:")
    print("  - connections")
    print("  - ssh_keys")
    print("  - ssh_sessions")
    print("  - Updated users and user_sessions with new relationships")


if __name__ == "__main__":
    main()
