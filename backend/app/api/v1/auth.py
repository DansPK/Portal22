from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.auth import LoginRequest, TokenResponse, MeResponse
from app.services.auth_service import create_user, authenticate, create_session
from app.database import get_db
from app.models.user import User
from app.api.deps import get_current_user

router = APIRouter()


@router.post("/setup", response_model=MeResponse)
def setup(username: str, password: str, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == username).first()
    if existing:
        raise HTTPException(status_code=400, detail="User exists")
    user = create_user(db, username, password)
    return MeResponse(id=user.id, username=user.username)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    user = authenticate(db, payload.username, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    session = create_session(db, user)
    return TokenResponse(access_token=session.token)


@router.get("/me", response_model=MeResponse)
def me(token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)
    return MeResponse(id=user.id, username=user.username)
