from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User, UserSession


def get_current_user(token: str, db: Session = Depends(get_db)) -> User:
    session = db.query(UserSession).filter(UserSession.token == token).first()
    if not session or not session.user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return session.user
