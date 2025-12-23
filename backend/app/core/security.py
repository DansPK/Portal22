from passlib.context import CryptContext
from cryptography.fernet import Fernet
import base64

# Prefer Argon2id for new hashes; keep pbkdf2_sha256 for verifying existing ones
pwd_context = CryptContext(schemes=["argon2", "pbkdf2_sha256"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def _derive_key(secret: str) -> bytes:
    # Quick-and-simple derivation to 32 bytes for Fernet
    data = secret.encode("utf-8")
    padded = (data + b"\0" * 32)[:32]
    return base64.urlsafe_b64encode(padded)


def encrypt(plaintext: str, secret: str) -> str:
    f = Fernet(_derive_key(secret))
    return f.encrypt(plaintext.encode("utf-8")).decode("utf-8")


def decrypt(token: str, secret: str) -> str:
    f = Fernet(_derive_key(secret))
    return f.decrypt(token.encode("utf-8")).decode("utf-8")
