def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_setup_and_login(client):
    r = client.post("/api/v1/auth/setup", params={"username": "alice", "password": "secret"})
    assert r.status_code == 200

    r = client.post("/api/v1/auth/login", json={"username": "alice", "password": "secret"})
    assert r.status_code == 200
    token = r.json()["access_token"]

    r = client.get("/api/v1/auth/me", params={"token": token})
    assert r.status_code == 200
    assert r.json()["username"] == "alice"
