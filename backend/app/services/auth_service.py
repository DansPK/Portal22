from sqlalchemy.orm import Session
from secrets import token_urlsafe
from datetime import datetime, timedelta

from app.core.security import hash_password, verify_password
from app.models.user import User, UserSession
from app.config import settings


def create_user(db: Session, username: str, password: str) -> User:
    user = User(username=username, hashed_password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def authenticate(db: Session, username: str, password: str) -> User | None:
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None


def create_session(db: Session, user: User) -> UserSession:
    token = token_urlsafe(32)
    expires = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    session = UserSession(user_id=user.id, token=token, expires_at=expires)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session
