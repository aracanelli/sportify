from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "email": "testuser@example.com",
            "password": "securepass123",
            "full_name": "Test User",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "testuser@example.com"
    assert "id" in data
