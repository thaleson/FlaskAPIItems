from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

# URL de conexão com o banco de dados SQLite
DATABASE_URL = "seu banco de dados"

# Objeto Metadata para gerenciar o esquema do banco de dados
metadata = MetaData()

# Criação do engine para o banco de dados
engine = create_engine(DATABASE_URL, echo=True)

# Criação do SessionLocal, que fornece sessões de banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
Database configuration for SQLAlchemy.

This module configures the connection to the SQLite database and sets up
the session factory for interacting with the database.

Dependencies:
- SQLAlchemy's create_engine to create a connection to the database.
- sessionmaker to create session objects for database operations.

Configuration:
- `DATABASE_URL`: The URL for the SQLite database file.
- `metadata`: An instance of SQLAlchemy's MetaData for managing database schema.
- `engine`: The SQLAlchemy engine connected to the SQLite database.
- `SessionLocal`: A session factory for creating new database sessions.
"""

# Observação: `database` é omitido porque não é necessário para SQLite local
