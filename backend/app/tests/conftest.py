import pytest
import pathlib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.database import Base
from app.main import app
from fastapi.testclient import TestClient
import os
from dotenv import load_dotenv

from alembic.config import Config
from alembic import command

load_dotenv(".env.test")  # ✅ Load the test .env file

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Run Alembic migrations before the first test
@pytest.fixture(scope="session", autouse=True)
def apply_migrations():
    base_dir = pathlib.Path(__file__).resolve().parent.parent.parent
    alembic_cfg = Config(os.path.join(base_dir, "alembic.ini"))  # ✅ fix path
    command.upgrade(alembic_cfg, "head")


@pytest.fixture(autouse=True)
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


@pytest.fixture()
def db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture()
def client():
    return TestClient(app)
