import os
import secrets
from datetime import datetime

from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app.models.user import User
from app.core.security import hash_password


DEFAULT_USERNAME_ENV = "PORTAL22_DEFAULT_USERNAME"
DEFAULT_PASSWORD_ENV = "PORTAL22_DEFAULT_PASSWORD"


def get_defaults() -> tuple[str, str, bool]:
    username = os.getenv(DEFAULT_USERNAME_ENV)
    password = os.getenv(DEFAULT_PASSWORD_ENV)
    generated = False
    if not username:
        username = "admin"
    if not password:
        password = secrets.token_urlsafe(16)
        generated = True
    return username, password, generated


def main() -> None:
    # Ensure tables exist
    Base.metadata.create_all(bind=engine)

    username, password, generated = get_defaults()

    db: Session = SessionLocal()
    try:
        existing = db.query(User).filter(User.username == username).first()
        if existing:
            print(f"User '{username}' already exists (id={existing.id}). Nothing to do.")
            return

        # Prepare credentials
        password_hash = hash_password(password)  # Argon2id (with PBKDF2 fallback available)
        # 32-byte salt for encryption key derivation (separate from password hash salt)
        salt = os.urandom(32)

        user = User(
            username=username,
            hashed_password=password_hash,
            master_password_hash=password_hash,
            salt=salt,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            last_login_at=None,
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        print("Default user created:")
        print(f"  username: {username}")
        print(f"  password: {password}{'  (generated)' if generated else ''}")
        print(f"  user_id: {user.id}")
        print("Keep these credentials safe. Consider rotating the password immediately.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
