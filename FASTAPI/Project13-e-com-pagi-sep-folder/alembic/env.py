import os
from dotenv import load_dotenv
from logging.config import fileConfig

from sqlalchemy import create_engine, pool
from alembic import context
from Models.Items import ItemsModel
from Models.Order import OrderModel
from Models.Product import ProductModel
from Models.Register import RegisterModel

# Load .env
load_dotenv()

config = context.config

# logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# IMPORT YOUR BASE HERE
from Database.db import Base   # <-- FIX PATH IF NEEDED

target_metadata = Base.metadata

# DB URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")


def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    connectable = create_engine(
        DATABASE_URL,
        poolclass=pool.NullPool
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()