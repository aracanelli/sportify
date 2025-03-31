from app.models.user import User


def test_user_model_fields():
    user = User(
        email="test@example.com", hashed_password="fakehash123", full_name="Test User"
    )

    assert user.email == "test@example.com"
    assert user.full_name == "Test User"
