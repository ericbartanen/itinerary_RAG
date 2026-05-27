from sqlalchemy import ForeignKey, String, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from pgvector.sqlalchemy import Vector

import datetime

class Base(DeclarativeBase):
    pass

class documents(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str] = mapped_column(String(255), nullable=False)
    source_path: Mapped[str] = mapped_column(String(255), nullable=False)
    content_hash: Mapped[str] = mapped_column(String, nullable=False)
    metadata: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False)

class document_chunks(Base):
    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(primary_key=True)
    document_id: Mapped[int] = mapped_column(ForeignKey("documents.id"), nullable=False)
    chunk_index: Mapped[int] = mapped_column(nullable=False)
    chunk_content: Mapped[str] = mapped_column(String, nullable=False)
    embedding: Mapped[Vector] = mapped_column(Vector(1536), nullable=False)
    metadata: Mapped[str] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False)
    updated_at: Mapped[datetime.datetime] = mapped_column(TIMESTAMP, nullable=False

    # Define the relationship to the documents table
    document: Mapped["documents"] = relationship("documents", back_populates="chunks")

