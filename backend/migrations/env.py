import os
from dotenv import load_dotenv

from sqlalchemy import engine_from_config, pool, create_engine
from logging.config import fileConfig

from alembic import context
from app.db.database import Base
from app.models.user import User  # Import your models here

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
print("📦 Using DATABASE_URL:", DATABASE_URL)

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_online():
    connectable = create_engine(DATABASE_URL)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
