from app.core.security import hash_password, verify_password, encrypt, decrypt


def test_password_hashing():
    pw = "secret"
    h = hash_password(pw)
    assert verify_password(pw, h)


def test_encrypt_decrypt():
    secret = "dev-secret-key"
    msg = "hello"
    token = encrypt(msg, secret)
    assert decrypt(token, secret) == msg
