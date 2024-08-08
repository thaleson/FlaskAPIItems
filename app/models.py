from sqlalchemy import Column, Integer, String
from .database import metadata, engine
from sqlalchemy.ext.declarative import declarative_base

# Criação da base para todos os modelos SQLAlchemy
Base = declarative_base(metadata=metadata)

class Item(Base):
    """
    Modelo para a tabela de itens no banco de dados.

    Attributes:
        id: Identificador único do item, chave primária e índice.
        name: Nome do item, indexado para pesquisa eficiente.
        description: Descrição do item, indexada para pesquisa eficiente.

    Table:
        items: Tabela no banco de dados que armazena informações sobre itens.
    """
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)

# Cria as tabelas no banco de dados com base nos modelos definidos
Base.metadata.create_all(bind=engine)
